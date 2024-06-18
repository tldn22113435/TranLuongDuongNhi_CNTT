<%-- 
    Document   : index
    Created on : May 31, 2024, 9:04:24 AM
    Author     : PHT
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<div class="row">
    <c:forEach var="product" items="${list}">
        <div class="col-sm-4 mt-3">
            <img src="<c:url value="/products/${product.id}.jpg" />" width="100%" />
            Id: ${product.id}<br/>
            Description: ${product.description}<br/>
            <strike>Old Price: <fmt:formatNumber value="${product.price}" type="currency" /></strike><br/>
            Discount: <fmt:formatNumber value="${product.discount}" type="percent" /><br/>
            <span style="color:red;font-size:18pt;">New Price: <fmt:formatNumber value="${product.price*(1 - product.discount)}" type="currency" /></span><br/>
            Category Id: ${product.categoryId}<br/>
            <a class="btn btn-primary" href="<c:url value="/cart/add?id=${product.id}" />"><i class="bi bi-cart-plus"></i> Add to Cart</a>
        </div>
    </c:forEach>
</div>