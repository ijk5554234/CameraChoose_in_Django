
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
<!--[if lte IE 8]><script src="css/ie/html5shiv.js"></script><![endif]-->
<script src="js/jquery.min.js"></script>
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
        <div class="col-md-8 col-md-offset-2">
            <h2 style="text-shadow:2px 2px gray; text-align:center">Do you want to take photographs like this picture?</h2>
                        <form method="POST" action="blind.do">
                        <div align="center" style="height:400px; margin:auto; margin-top:50px">
                        <img class="center" style="height:100%" src="${picture.url}" /> <input type="hidden" name="url"
                            value="${picture.url}" /> <input type="hidden" name="camera"
                            value="${picture.camera}" /> <input type="hidden" name="like"
                            value="${picture.like}" />
                        </div>
                          <div  class="col-md-4 col-md-offset-4">
                        <button  class="btn btn-success btn-raised" type="submit" name="action" value="like">Like</button>
                        <button  class="btn btn-default btn-raised" type="submit" name="action" value="dislike" style="color:white">Dislike it</button>
                        </div>
                    </form>
        </div><!-- /pagewrap -->
    </body>
</html>