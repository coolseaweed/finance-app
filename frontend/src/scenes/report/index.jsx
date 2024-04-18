import { Box, Typography, useTheme } from "@mui/material";
import { styled } from "@mui/material/styles";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell, { tableCellClasses } from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { mockKospiData as data } from "../../data/mockData";
import Header from "../../components/Header";
import { tokens } from "../../theme";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.common.black,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(odd)": {
    backgroundColor: theme.palette.action.hover,
  },
  // hide last border
  "&:last-child td, &:last-child th": {
    border: 0,
  },
}));

const Report = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <Box m="20px">
      <Header title="REPORT" subtitle="Overview finance statement report" />
      <Box m="40px 0 0 0" height="75vh">
        <Typography
          variant="h2"
          color={colors.grey[500]}
          fontWeight="bold"
          sx={{ m: "0 0 5px 0" }}
        >
          재무제표
        </Typography>
        <TableContainer component={Paper}>
          <Table sx={{ minWidth: 700 }} aria-label="customized table">
            <TableHead>
              <TableRow>
                <StyledTableCell>IFRS(연결)</StyledTableCell>
                <StyledTableCell align="right">2021/12</StyledTableCell>
                <StyledTableCell align="right">2022/12</StyledTableCell>
                <StyledTableCell align="right">2023/12</StyledTableCell>
                <StyledTableCell align="right">전년동기(%)</StyledTableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {data.map((row) => (
                <StyledTableRow key={row.field}>
                  <StyledTableCell component="th" scope="row">
                    {row.field}
                  </StyledTableCell>
                  <StyledTableCell align="right">{row.before}</StyledTableCell>
                  <StyledTableCell align="right">{row.last}</StyledTableCell>
                  <StyledTableCell align="right">{row.this}</StyledTableCell>
                  <StyledTableCell align="right">{row.diff}</StyledTableCell>
                </StyledTableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Box>
  );
};

export default Report;
