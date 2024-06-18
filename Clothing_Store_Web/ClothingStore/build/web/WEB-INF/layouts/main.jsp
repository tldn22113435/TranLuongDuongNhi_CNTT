<%-- 
    Document   : main
    Created on : May 3, 2024, 9:00:44 AM
    Author     : PHT
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    <h1 style="color:red;">
                        Clothing store
                        <a href="<c:url value="/cart/index" />">
                            <span class="float-end" style="color:black;font-size:14pt;padding-top: 20px;">Your cart: <fmt:formatNumber value="${cart.totalCost}" type="currency" /></span>
                        </a>
                    </h1>                    
                    <hr/>
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <%--insert view here--%>
                    <jsp:include page="/WEB-INF/views/${controller}/${action}.jsp" />
                </div>
            </div>
            <div class="row">
                <div class="col-sm-12">
                    <hr/>
                    © 2024 - CÔNG TY TNHH DUONG NHI
                    <hr/>
                    Giấy CNĐKDN: 0310874931 – Ngày cấp: 25/11/2011 - Cơ quan cấp: Phòng Đăng Ký Kinh Doanh – Sở Kế Hoạch và Đầu Tư TP.HCM
                    <hr/>
                    Địa chỉ đăng ký kinh doanh: 112 Đường Sư Vạn Hạnh, Phường 12, Quận 10, TP.HCM - Điện thoại: 19002004532 - Mua hàng: 19002004532 - Email: cskh@duongnhi.vn
                    <hr/>
                </div>
            </div>
        </div>
    </body>
</html>
