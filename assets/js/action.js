var inputImg =  document.getElementById("inputImage");
var inputImageBtn = document.getElementById("inputImageBtn");
var imageName = document.getElementById("image-name");

inputImg.addEventListener("change", (e) => {
    console.log(e.target.files[0].name);
    imageName.innerHTML = e.target.files[0].name;
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(e.target.files[0]);
});

inputImageBtn.addEventListener("click", () => {
    document.getElementById("inputImage").click();
    //inputImg.change();
});
