var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var http_req = new XMLHttpRequest();
http_req.open("GET", "http://coolseaweed.iptime.org:10080/dummy");
http_req.send();
http_req.onreadystatechange = (e) => {
  console.log(http_req.responseText);
};
