window.addEventListener("load", () =>{
    var canvas = document.getElementById('paint');
    var ctx = canvas.getContext('2d');

    var painting = document.getElementById('frame');
    var paint_style = getComputedStyle(painting);
    canvas.width = parseInt(paint_style.getPropertyValue('width'));
    canvas.height = parseInt(paint_style.getPropertyValue('height'));
    var mouse = {x: 0, y: 0};

    var painting = false;

    function start(){
        painting = true;
        draw(e);
    }
    function finished(){
        painting = false;
        ctx.beginPath();
        getData()
    }

    function draw(e){
        if(!painting) return;
        mouse.x = e.pageX - this.offsetLeft;
        mouse.y = e.pageY - this.offsetTop;
        ctx.lineWidth = 20;
        ctx.lineCap = 'round';
        ctx.strokeStyle = '#ff0000';
        ctx.lineTo(mouse.x,mouse.y);
        ctx.stroke();
        ctx.beginPath();
        ctx.moveTo(mouse.x,mouse.y);
    }

    function getData(){
        $.post("img_data/", {data: canvas.toDataURL("image/png")}).done(function(data) {
          $("#number").html(data);
      });
    }

    $('#c_button').click(function(){
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      $('#number').html('');
    });

    //Listeners
    canvas.addEventListener("mousedown",start);
    canvas.addEventListener("mouseup",finished);
    canvas.addEventListener("mousemove",draw);

});
 