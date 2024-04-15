import "./css/App.css";
import "./css/table.css";
import { useState, useEffect } from "react";
import DataTable from "./components/dataTable";
import { BrowserRouter, Routes, Route } from "react-router-dom";

const headers = [
  {
    text: "Name",
    value: "name",
  },
  {
    text: "Version",
    value: "version",
  },
  {
    text: "Launch Date",
    value: "launch",
  },
];
const items = [
  {
    name: "React",
    version: "18.2.0",
    launch: "2013-05-29",
  },
  {
    name: "Vue",
    version: "3.2.45",
    launch: "2014-02",
  },
  {
    name: "jQuery",
    version: "3.3",
    disabled: true,
    launch: "2006-08-26",
  },
  {
    name: "Svelte",
    version: "3.53.1",
    launch: "2016-11-26",
  },
];

function App() {
  let post = "강남 우동 맛집";
  let [title, setTitle] = useState([
    "남자 코트 추천",
    "여자 코트 추천",
    "파이썬독학",
  ]);
  let [like, setLike] = useState(0);

  const [selection, setSelection] = useState([]);
  useEffect(() => {
    console.log(selection);
  }, [selection]);

  function addOne() {
    setLike(like + 1);
  }

  return (
    <div className="App">
      <div className="black-nav">
        <h4 style={{ color: "white", fontSize: "16px" }}>React Test Blog</h4>
      </div>
      <div className="list">
        <h4>
          {title[0]}
          <span onClick={addOne}> 👍</span> {like}
        </h4>
        <p>2월 17일 발행</p>
        <h4>{title[1]}</h4>
        <p>2월 17일 발행</p>
        <h4>{title[2]}</h4>
        <p>2월 17일 발행</p>
      </div>
      <Modal />
      <Modal />
      <DataTable
        headers={headers}
        items={items}
        selectable={true}
        updateSelection={setSelection}
      />

      <h4>{post}</h4>
    </div>
  );
}

function Modal() {
  return (
    <div className="modal">
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  );
}

export default App;
