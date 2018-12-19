<%@ page  import= "DTO.Image,DTO.ListImage" %>
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Result page</title>
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>
</head>
<body>
<%ListImage lst = (ListImage) request.getAttribute("listImage");  
	int tile = (int) request.getAttribute("tile");%>
		<div> 
			<center><h3>Image Search </h3></center>
<table style="width:30%">
  <tr>
    <th>Result</th>
    <th>Ratio</th> 
    
  </tr>
  <tr>
  <td> </td>
    <td><%=tile %>/100</td>
    
  </tr>
  
</table>
			<center><img alt="#" src="<%=lst.getLstImage().get(0).getUrlImage().toString()%>" width= "240" height = "240">
			</center>
			</br></br>
		</div>
	<div>
	<h3>Result </h3>
			  <%  
					
					for(int i = 0 ; i < lst.getLstImage().size();i++)
					{	
						String size = new String("width = ' "+ 80 +"'"+"height = '" +80 +"'");
						
						out.println("<img src= '" + lst.getLstImage().get(i).getUrlImage().toString() + "'"+ size + "/>");
					}
					%> 
					
	</div>
</body>
</html>