USE [products_db];
GO

-- Drop table if exists
IF OBJECT_ID('products', 'U') IS NOT NULL
    DROP TABLE [products];
GO

-- Create products table
CREATE TABLE [products] (
    [ID] INT IDENTITY(1,1) PRIMARY KEY,
    [Discount] DECIMAL(5,2),
    [Purchase_Price] DECIMAL(10,2),
    [Selling_Price] DECIMAL(10,2),
    [Product_Name] NVARCHAR(255)
);
GO

-- Sample products for testing
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 147.67, 147.67, N'كيلو كريتال لمع ابيض 101');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 380');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 310');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 404');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 410');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 492');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 240');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 204');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 210');
INSERT INTO [products] ([Discount], [Purchase_Price], [Selling_Price], [Product_Name]) VALUES (0, 100.63, 100.63, N'كيلو كريتال لمع 205');
