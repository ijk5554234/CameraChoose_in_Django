<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>
<%@ page import="databeans.PictureBean"%>
<!DOCTYPE HTML>
<html>
<head>
<title>Camera Choose-blindtest</title>
<meta name="viewport" content="width=1200,user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta name="description" content="" />
<meta name="keywords" content="" />
<link href="css/bootstrap.min.css" rel="stylesheet">
<link href="css/ripples.min.css" rel="stylesheet">
<link href="css/material-wfont.min.css" rel="stylesheet">
<link rel="stylesheet" type="text/css" href="css/lb.css" media="all" />
<!--页面整体样式-->
<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
<script type="text/javascript" src="js/jquery.min.js"></script>

<script src="js/jquery.poptrox.min.js"></script>
<script src="js/skel.min.js"></script>
<script src="js/init.js"></script>
<script src="js/bootstrap.min.js"></script>
<script src="js/ripples.min.js"></script>
<script src="js/material.min.js"></script>
<script>
    $(document).ready(function() {
        $.material.init();
    });
</script>
<noscript>
	<link rel="stylesheet" href="css/skel.css" />
	<link rel="stylesheet" href="css/style.css" />
	<link rel="stylesheet" href="css/style-desktop.css" />
	<link rel="stylesheet" href="css/style-noscript.css" />
</noscript>
<!--[if lte IE 8]><link rel="stylesheet" href="css/ie/v8.css" /><![endif]-->
</head>

<body>
	<h1 align="center" style="text-shadow: 1px 0 1px #8B4513">Congrats!
		The camera we recommend is ${camera.model}</h1>
	<!-- <blockquote>
		<c:forEach var="t" items="${tweets}">
			<p>${t}</p>
		</c:forEach>
	</blockquote> -->

	<section id="gallery">
		<div class="container_image">
			<ul id="myRoundabout">
				<li><script type="text/javascript"
						src="https://www.google.com/jsapi"></script> <script
						type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable(); 
          data.addColumn('date', 'Date');
          data.addColumn('number','${camera1name}' );
          data.addColumn('number','${camera2name}' );  
          <c:forEach var="record" items="${DateRecords}"> 
          data.addRow([ new Date(${record.date}),  ${record.camera1Num}, ${record.camera2Num}]);
          </c:forEach>  

       var options = {
          title: 'Camera Choose',
          hAxis: {title: 'Date',  titleTextStyle: {color: '#333'}},
          vAxis: {minValue: 0}
        };

        var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
         
    </script>
					<div id="chart_div"></div></li>
				<li><script type="text/javascript"
						src="https://www.google.com/jsapi"></script> <script
						type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
       
        function drawChart() {
          var camera1Times = ${camera1Times};
          var camera2Times = ${camera2Times};
        var data = google.visualization.arrayToDataTable([
          ['Camera', 'Choose Result'],
          ['${camera1name}', camera1Times ],
          ['${camera2name}', camera2Times],
        ]);

        var options = {
          title: 'Camera Choose Statistics',
          is3D: true,
          pieSliceText: 'label', //on mouse hover show label or name of the Country
          tooltip :  {showColorCode: true}, 
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
      } 
        </script>
					<div id="piechart_3d"></div></li>
				<li><script type="text/javascript"
						src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization','version':'1','packages':['corechart']}]}"></script>
					<script type="text/javascript">            
    google.load('visualization', '1', {packages: ['corechart']});
    google.setOnLoadCallback(drawChart);
    function drawChart() {
      var camera1Num = ${camera1SearchNum};
      var camera2Num = ${camera2SearchNum};
      var data = google.visualization.arrayToDataTable([
        ['Camera',          'Search Heat Rate'],
        ['${camera1name}',       camera1Num ],
        ['${camera2name}',       camera2Num ]      
      ]);

      var options = {
        title: 'Search Heat Rate In Google',
        
        hAxis: {
          title: 'Total Search Volume',
          minValue: 0
        },
        vAxis: {
          title: 'Camera'
        }
      };

      var chart = new google.visualization.BarChart(
        document.getElementById('ex0'));

      chart.draw(data, options);
    }
    </script>
					<div id="ex0"></div></li>
			</ul>
		</div>
	</section>


	<div class="col-md-8 col-md-offset-2">
		<form class="form-horizontal" action="result.do" method="post">

			<fieldset>
				<h4>
					Share your test result to your friends on
					Twitter!&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<a
						href="logout.do">Logout</a>
				</h4>
				<textarea align="center" class="form-control" rows="3" id="textArea"
					name="text">
        I got a test on CameraChoose and the best camera for me is ${camera.model}! Try it on www.camerachoose.com!
        </textarea>
				<div class="form-group" style="margin-bottom: 0px;">
					<div align="right" class="col-lg-10 col-lg-offset-2">
						<a class="btn btn-default btn-sm" style="color: white" href="compare.do">Test
							again!</a>
						<button type="submit" name="action" value="tweet"
							class="btn btn-primary btn-sm">Share!</button>
					</div>
				</div>
			</fieldset>
		</form>
	</div>







	<script src="//code.jquery.com/jquery-1.10.2.min.js"></script>
	<script
		src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>

	<script src="js/ripples.min.js"></script>
	<script src="js/material.min.js"></script>
	<script type="text/javascript" src="js/jquery-1.4.2.min.js"></script>
	<script type="text/javascript" src="js/roundabout.js"></script>
	<!--中间广告图片2-->
	<script type="text/javascript" src="js/roundabout_shapes.js"></script>
	<!--中间广告图片3-->
	<script type="text/javascript" src="js/gallery_init.js"></script>
	<!--中间广告图片4-->
</body>

</html>