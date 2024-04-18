import { Box, Typography, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { tokens } from "../../theme";
import {
  mockKospiData as kospi,
  mockKosdaqData as kosdaq,
} from "../../data/mockData";
import Checkbox from "@mui/material/Checkbox";
import Header from "../../components/Header";
import { useState } from "react";
import FormControlLabel from "@mui/material/FormControlLabel";
import { columns, initColumns } from "./metaData";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtons from "../../components/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";

const Filter = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [visibleColumns, setVisibleColumns] = useState(initColumns);
  const [isKospi, setMarket] = useState(true);
  const [alignment, setAlignment] = useState("left");

  const handleChange = (event) => {
    const field = event.target.name;
    const checked = event.target.checked;

    visibleColumns[field] = checked;
    setVisibleColumns((prev) => ({ ...prev }));
  };

  const handleAlignment = (event, newAlignment) => {
    setAlignment(newAlignment);
  };
  return (
    <Box m="20px">
      <Header title="Filter" subtitle="Filtering korean stock market" />

      {/* CHECK BOXES  */}
      <Box
        sx={{
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        {columns
          .filter((column) => column.field !== "name")
          .map((column) => (
            <FormControlLabel
              control={
                <Checkbox
                  defaultChecked={column.defaultChecked}
                  onChange={handleChange}
                  name={column.field}
                />
              }
              label={column.headerName}
            />
          ))}
      </Box>

      {/* DATA GRID */}
      <Box
        m="40px 0 0 0"
        height="75vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .name-column--cell": {
            color: colors.greenAccent[300],
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: colors.blueAccent[700],
            borderBottom: "none",
          },
          "& .MuiDataGrid-virtualScroller": {
            backgroundColor: colors.primary[400],
          },
          "& .MuiDataGrid-footerContainer": {
            borderTop: "none",
            backgroundColor: colors.blueAccent[700],
          },
          "& .MuiCheckbox-root": {
            color: `${colors.greenAccent[200]} !important`,
          },
        }}
      >
        <ToggleButtonGroup
          value={alignment}
          exclusive
          onChange={handleAlignment}
          aria-label="text alignment"
        >
          <ToggleButton
            value="left"
            aria-label="left aligned"
            onClick={() => setMarket(true)}
          >
            코스피
          </ToggleButton>
          <ToggleButton
            value="center"
            aria-label="centered"
            onClick={() => setMarket(false)}
          >
            코스닥
          </ToggleButton>
        </ToggleButtonGroup>

        <DataGrid
          getRowId={isKospi ? (kospi) => kospi.name : (kosdaq) => kosdaq.name}
          rows={isKospi ? kospi : kosdaq}
          columns={columns}
          columnVisibilityModel={visibleColumns}
          onColumnVisibilityModelChange={(newModel) =>
            setVisibleColumns(newModel)
          }
        />
      </Box>
    </Box>
  );
};

export default Filter;
