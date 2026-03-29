function showMore() {
  var pageCur = Number(document.getElementById("page-cur").value);
  // var pageNum = Number(document.getElementById("page-num").value);

  pageCur += 1;
  fetch("?page=" + pageCur, { headers: { "X-Requested-With": "XMLHttpRequest" } })
    .then((response) => {
      console.log(response);
      if (!response.ok) {
        throw new Error("Network response was not ok" + response.statusText);
      }
      return response.text();
    })
    .then((data) => {
      document.getElementsByClassName("post-container")[0].innerHTML += data;
      // document.getElementsByClassName("post-container")[0].insertAdjacentHTML("beforeend", data);
      document.getElementById("page-cur").value = pageCur;
    });
}
