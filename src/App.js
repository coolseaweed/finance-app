import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {

  let post = '강남 우동 맛집';
  let [title, setTitle] = useState(['남자 코트 추천', '여자 코트 추천', '파이썬독학']);
  let [like, setLike] = useState(0);

  function addOne() {
    setLike(like + 1)
  }



  return (
    <div className="App">
      <div className="black-nav">
        <h4 style={{ color: 'white', fontSize: '16px' }}>React Test Blog</h4>
      </div>
      <div className='list'>
        <h4>{title[0]}
          <span onClick={addOne}> 👍</span> {like}
        </h4>
        <p>2월 17일 발행</p>
        <h4>{title[1]}</h4>
        <p>2월 17일 발행</p>
        <h4>{title[2]}</h4>
        <p>2월 17일 발행</p>
      </div>



      <Modal></Modal>

      <h4>{post}</h4>
    </div>
  );
}



function Modal() {
  return (
    <div className='modal'>
      <h4>제목</h4>
      <p>날짜</p>
      <p>상세내용</p>
    </div>
  )
}

export default App;
