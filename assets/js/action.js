//var inputImg =  document.getElementById("inputImage");
var inputImg =  document.getElementById("id_imagen");
var inputImageBtn = document.getElementById("inputImageBtn");
var imageName = document.getElementById("image-name");

inputImg.addEventListener("change", (e) => {
    imageName.innerHTML = e.target.files[0].name;
    var image = document.getElementById('output');
	image.src = URL.createObjectURL(e.target.files[0]);
});

inputImageBtn.addEventListener("click", () => {
    document.getElementById("id_imagen").click();
    var result = document.getElementById("result");
    var contName = document.getElementById("cont-imagen-name");
    result.style.display = "none";
    result.style.visibility= "hidden";
    contName.style.visibility= "visible";
    contName.style.display= "block";
    //document.getElementById("inputImage").click();
});
