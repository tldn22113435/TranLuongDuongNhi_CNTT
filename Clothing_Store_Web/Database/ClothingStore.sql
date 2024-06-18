raiserror('Creating ClothingStore database....',0,1)
SET NOCOUNT ON
GO
USE [master]
GO
CREATE DATABASE [ClothingStore]
GO
USE [ClothingStore]
GO
CREATE TABLE [dbo].[Category](
	[id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[name] [varchar](50) NOT NULL
)
GO
CREATE TABLE [dbo].[Product](
	[id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[description] [varchar](50) NOT NULL,
	[price] [float] NOT NULL,
	[discount] [float] NOT NULL,
	[categoryId] [int] references Category(id) NOT NULL
)
GO
CREATE TABLE [dbo].[Account](
	[id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[name] [varchar](50) NOT NULL,
	[address] [varchar](50) NOT NULL,
	[phone] [varchar](12) NOT NULL,
	[email] [varchar](30) NOT NULL,
	--password: default = 1
	[password] [char](64) NOT NULL default('6B86B273FF34FCE19D6B804EFF5A3F5747ADA4EAA22F1D49C01E52DDB7875B4B'),
	[enabled] [bit] NOT NULL default(1),
	[role] [varchar](255) NOT NULL
)
GO
CREATE TABLE [dbo].[Customer](
	[id] [int] PRIMARY KEY references [Account](id) NOT NULL,
	[category] varchar(50) NOT NULL CHECK([category] IN ('Gold','Silver','Copper')),
	[shipToAddress] [varchar](50) NOT NULL
)
GO
CREATE TABLE [dbo].[Employee](
	[id] [int] PRIMARY KEY references [Account](id) NOT NULL,
	[salary] [money] NOT NULL,
	[departmentId] [int] NOT NULL
)
GO
CREATE TABLE [dbo].[OrderHeader](
	[id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[date] [datetime] NOT NULL,
	[status] [varchar](30) NULL,
	[customerId] [int] references Customer(id) NOT NULL,
	[employeeId] [int] references Employee(id) NOT NULL
)
GO
CREATE TABLE [dbo].[OrderDetail](
	[id] [int] IDENTITY(1,1) PRIMARY KEY NOT NULL,
	[orderHeaderId] [int] references OrderHeader(id) NOT NULL,
	[productId] [int] references Product(id) NOT NULL,
	[quantity] [int] NOT NULL,
	[price] [float] NOT NULL,
	[discount] [float] NOT NULL
)
GO
SET IDENTITY_INSERT [dbo].[Category] ON 

INSERT [dbo].[Category] ([id], [name]) VALUES (1, N'Shirt')
INSERT [dbo].[Category] ([id], [name]) VALUES (2, N'Pants')
INSERT [dbo].[Category] ([id], [name]) VALUES (3, N'Underwear')
SET IDENTITY_INSERT [dbo].[Category] OFF
SET IDENTITY_INSERT [dbo].[Product] ON 

INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (1, N'T-shirt 1', 150.24, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (2, N'T-shirt 2', 152.21, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (3, N'T-shirt 3', 151.28, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (4, N'Shirt 1', 201.41, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (5, N'Shirt 2', 203.63, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (6, N'Shirt 3', 206.13, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (7, N'Jacket 1', 188.19, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (8, N'Jacket 2', 182.99, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (9, N'Jacket 3', 186.25, 0.05, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (10, N'Vest 1', 1000.23, 0, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (11, N'Vest 2', 1080.11, 0, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (12, N'Vest 3', 1500.54, 0, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (13, N'Blazer 1', 301.41, 0.15, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (14, N'Blazer 2', 305.53, 0.15, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (15, N'Blazer 3', 305.12, 0.15, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (16, N'Hoodie 1', 599.99, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (17, N'Hoodie 2', 599.99, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (18, N'Hoodie 3', 599.99, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (19, N'Sweater 1', 414.42, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (20, N'Sweater 2', 431.54, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (21, N'Sweater 3', 477.12, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (22, N'Tank top 1', 91.12, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (23, N'Tank top 2', 96.24, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (24, N'Tank top 3', 93.35, 0.1, 1)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (25, N'Kaki pant 1', 211.93, 0.1, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (26, N'Kaki pant 2', 223.55, 0.1, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (27, N'Kaki pant 3', 215.64, 0.1, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (28, N'Jogger pants 1', 165.23, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (29, N'Jogger pants 2', 125.54, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (30, N'Jogger pants 3', 179.26, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (31, N'Short jeans 1', 79.68, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (32, N'Short jeans 2', 80.28, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (33, N'Short jeans 3', 78.96, 0.05, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (34, N'Trousers 1', 229.11, 0, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (35, N'Trousers 2', 200.56, 0, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (36, N'Trousers 3', 215.87, 0, 2)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (37, N'Underwear 1', 59.88, 0, 3)
INSERT [dbo].[Product] ([id], [description], [price], [discount], [categoryId]) VALUES (38, N'Underwear 2', 61.54, 0, 3)

SET IDENTITY_INSERT [dbo].[Product] OFF

SET IDENTITY_INSERT [dbo].[Account] ON 
INSERT [dbo].[Account] ([id], [name], [address], [phone], [email], [role]) VALUES
(1, N'Admin', N'1600 Pennsylvania Avenue NW, Washington, DC 20500', N'555-0110', N'alex.smith123@gmail.com', 'ROLE_ADMIN'),
(2, N'Employee1', N'350 Fifth Avenue, New York, NY 10118', N'555-0198', N'emma.johnson88@gmail.com', 'ROLE_EMPLOYEE'),
(3, N'Employee2', N'1 Infinite Loop, Cupertino, CA 95014', N'555-0143', N'noah.brown2024@gmail.com', 'ROLE_EMPLOYEE'),
(4, N'Customer1', N'4059 Mt Lee Dr, Los Angeles, CA 90068', N'555-0179', N'sophia.williams77@gmail.com','ROLE_CUSTOMER'),
(5, N'Customer2', N'1000 5th Ave, New York, NY 10028', N'555-0186', N'oliver.davis56@gmail.com', 'ROLE_CUSTOMER')
SET IDENTITY_INSERT [dbo].[Account] OFF

INSERT [dbo].[Customer] ([id], [category], [shipToAddress]) VALUES (4, 'Copper', N'4059 Mt Lee Dr, Los Angeles, CA 90068')
INSERT [dbo].[Customer] ([id], [category], [shipToAddress]) VALUES (5, 'Copper', N'1000 5th Ave, New York, NY 10028')

INSERT [dbo].[Employee] ([id], [salary], [departmentId]) VALUES 
(1, 2000, 1),(2, 1500, 2),(3, 1000, 2)
GO
SET NOCOUNT OFF
raiserror('The ClothingStore database in now ready for use.',0,1)
GO

