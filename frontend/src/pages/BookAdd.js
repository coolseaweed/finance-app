import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";

export default function BookAdd() {
  const [bookId, setBookId] = useState("");
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [publisher, setPublisher] = useState("");
  const [releaseDate, setReleaseDate] = useState("");
  const [isbn, setIsbn] = useState("");

  const navigate = useNavigate();

  const handleSave = (event) => {
    event.preventDefault();
    const newBook = {
      bookId: bookId,
      title: title,
      author: author,
      publisher: publisher,
      releaseDate: releaseDate,
      isbn: isbn,
    };
    axios
      .post("/", newBook)
      .then((response) => {
        console.log("Book added successfully.");
        navigate("/list");
      })
      .catch((error) => {
        console.log("Error while adding book:", error);
      });
  };

  return (
    <div className="container">
      <h2 className="text-center mt-5 mb-3">Book 등록</h2>
      <div className="card">
        <div className="card-header">
          <Link className="btn btn-outline-primary mx-1" to="/">
            Home
          </Link>
          <Link className="btn btn-outline-primary mx-1" to="/list">
            Book 목록
          </Link>
        </div>
        <div className="card-body">
          <form>
            <div className="form-group">
              <label htmlFor="bookId">ID</label>
              <input
                onChange={(event) => {
                  setBookId(event.target.value);
                }}
                value={bookId}
                type="text"
                className="form-control"
                id="bookId"
                name="bookId"
                required
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="title">제목</label>
              <input
                onChange={(event) => {
                  setTitle(event.target.value);
                }}
                value={title}
                type="text"
                className="form-control"
                id="title"
                name="title"
                required
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="author">저자</label>
              <input
                onChange={(event) => {
                  setAuthor(event.target.value);
                }}
                value={author}
                type="text"
                className="form-control"
                id="author"
                name="author"
                required
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="publisher">출판사</label>
              <input
                onChange={(event) => {
                  setPublisher(event.target.value);
                }}
                value={publisher}
                type="text"
                className="form-control"
                id="publisher"
                name="publisher"
                required
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="releaseDate">출판일</label>
              <input
                onChange={(event) => {
                  setReleaseDate(event.target.value);
                }}
                value={releaseDate}
                type="text"
                className="form-control"
                id="releaseDate"
                name="releaseDate"
                required
              ></input>
            </div>
            <div className="form-group">
              <label htmlFor="isbn">ISBN</label>
              <input
                onChange={(event) => {
                  setIsbn(event.target.value);
                }}
                value={isbn}
                type="text"
                className="form-control"
                id="isbn"
                name="isbn"
                required
              ></input>
            </div>
            <button
              onClick={handleSave}
              type="button"
              className="btn btn-outline-primary mt-3"
            >
              저장
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
