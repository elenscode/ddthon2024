import "./App.css";

function App() {
  const handleButtonClick = () => {
    const iframe = document.getElementById("iframe1");
    console.log(iframe.contentWindow)
    const inputElement = iframe.contentWindow.document.getElementById("abcef");
    console.log(inputElement)
    if (inputElement) {
      inputElement.value = "새로운 값";
    }
  };

  return (
    <div className="app">
      <div className="item">
        React 영역
        <button onClick={handleButtonClick}>내용 추가</button>
      </div>
      <div className="item">
        <iframe
          id="iframe1"
          src="http://localhost:8501/?embed=true&embed_options=show_toolbar"
          height="800"
          style={{ width: "100%", border: "none" }}
        ></iframe>
      </div>
    </div>
  );
}

export default App;
