<%-- 
    Document   : index
    Created on : May 31, 2024, 9:47:22 AM
    Author     : PHT
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<h2>Your Cart</h2>
<hr/>
<table class="table table-striped">
    <tr>
        <th>#</th>
        <th>Id</th>
        <th>Image</th>
        <th>Description</th>
        <th style="text-align: right;">Old Price</th>
        <th style="text-align: right;">Discount</th>
        <th style="text-align: right;">New Price</th>
        <th style="text-align: right;">Cost</th>
        <th>Operations</th>
    </tr>
    <c:forEach var="item" items="${cart.list}" varStatus="loop">
        <tr>
            <td>${loop.count}</td>
            <td>${item.product.id}</td>
            <td><img src="<c:url value="/products/${item.product.id}.jpg" />" height="80"/></td>        
            <td>${item.product.description}</td>
            <td style="text-align: right;">
                <fmt:formatNumber value="${item.oldPrice}" type="currency"/>
            </td>
            <td style="text-align: right;">
                <fmt:formatNumber value="${item.discount}" type="percent"/>
            </td>
            <td style="text-align: right;">
                <fmt:formatNumber value="${item.newPrice}" type="currency"/>
            </td>
            <td style="text-align: right;">
                <fmt:formatNumber value="${item.cost}" type="currency"/>
            </td>
            <td>
                <a href="">Update</a>
                <a href="<c:url value="/cart/delete?id=${item.product.id}" />">Delete</a>
            </td>
        </tr>
    </c:forEach>
</table>
