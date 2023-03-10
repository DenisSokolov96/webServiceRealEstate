var myCanvas = document.getElementById("myCanvas");
myCanvas.width = 500;
myCanvas.height = 300;

var ctx = myCanvas.getContext("2d");

function drawLine(ctx, startX, startY, endX, endY,color){
    ctx.save();
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.moveTo(startX,startY);
    ctx.lineTo(endX,endY);
    ctx.stroke();
    ctx.restore();
}
function drawBar(ctx, upperLeftCornerX, upperLeftCornerY, width, height,color){
    ctx.save();
    ctx.fillStyle=color;
    ctx.fillRect(upperLeftCornerX,upperLeftCornerY,width-width*0.05,height);
    ctx.restore();
}

var str =  document.getElementById("myVar").value;
str = str.slice(1, -1);
str = str.split("'").join("").split(" ").join("");
str = str.split(",");
var myVinyls = new Map();
for (var el of str) {
    var tempMas = el.split(":");
    myVinyls[tempMas[0]] = tempMas[1];
}

var Barchart = function(options){
    this.options = options;
    this.canvas = options.canvas;
    this.ctx = this.canvas.getContext("2d");
    this.colors = options.colors;

    this.draw = function(){
        var maxValue = 0;
        for (var categ in this.options.data){
            maxValue = Math.max(maxValue,this.options.data[categ]);
        }
        var canvasActualHeight = this.canvas.height - this.options.padding * 2;
        var canvasActualWidth = this.canvas.width - this.options.padding * 2;
        //drawing the grid lines
        var gridValue = 0;
        while (gridValue <= maxValue){
            var gridY = canvasActualHeight * (1 - gridValue/maxValue) + this.options.padding;
            drawLine(
                this.ctx,
                0,
                gridY,
                this.canvas.width,
                gridY,
                this.options.gridColor
            );

            //writing grid markers
            this.ctx.save();
            this.ctx.fillStyle = this.options.gridColor;
            this.ctx.font = "bold 10px Arial";
            this.ctx.fillText(gridValue, 10,gridY - 2);
            this.ctx.restore();
            gridValue+=this.options.gridScale;
        }

        //drawing the bars
        var barIndex = 0;
        var numberOfBars = Object.keys(this.options.data).length;
        var barSize = (canvasActualWidth)/numberOfBars;
        for (categ in this.options.data){
            var val = this.options.data[categ];
            var barHeight = Math.round( canvasActualHeight * val/maxValue);
            drawBar(
                this.ctx,
                this.options.padding + barIndex * barSize,
                this.canvas.height - barHeight - this.options.padding,
                barSize,
                barHeight,
                this.colors[barIndex%this.colors.length]
            );
            barIndex++;
        }

        //drawing series name
        this.ctx.save();
        this.ctx.textBaseline="bottom";
        this.ctx.textAlign="center";
        this.ctx.fillStyle = "#000000";
        this.ctx.font = "bold 15px Arial";
        this.ctx.fillText(this.options.seriesName, this.canvas.width/2,this.canvas.height);
        this.ctx.restore();

        //draw legend
        barIndex = 0;
        var legend = document.querySelector("legend[for='myCanvas']");
        var ul = document.createElement("ul");
        legend.append(ul);
        var i = 0
        for (categ in this.options.data){
            var li = document.createElement("li");
            // if (i%2 !== 0) li = document.createElement("a");
            // else li = document.createElement("li");
            i++;
            li.style.listStyle = "none";
            li.style.borderLeft = "40px solid "+this.colors[barIndex%this.colors.length];
            li.style.padding = "5px";
            li.textContent = categ;
            ul.append(li);
            barIndex++;
        }

    }
}
var myBarchart = new Barchart(
    {
        canvas:myCanvas,
        seriesName:"????????????",
        padding:20,
        gridScale: 4,
        gridColor:"#000301",
        data:myVinyls,
        colors:["#cbc359","#eb9743", "#0b3aa6", "#67b6c7"]
    }
);
myBarchart.draw();