!pip install --trusted-host pypi.org ipython-sql 

%load_ext sql

%sql sqlite:///vbo.db


# ***************** 1. Find the total earnings earned by customers living in the USA ?  *****************

%%sql 
select sum(p.Price)
from Customers c
left join Orders o on o.CustomerID=c.CustomerID
left join OrderDetails od on od.OrderID=o.OrderID
left join Products  p on p.ProductID=od.ProductID
where Country='USA';


# ----------------------------------------------------------------------------------------------------------------


# ************* 2. Find the names of the CategoryIDs in the Products table and then show the average
#                                           product price per category ?   *************




%sql select avg(Price),CategoryName from Products p left join Categories c on c.CategoryID=p.CategoryID group by CategoryName;


# ----------------------------------------------------------------------------------------------------------------


# ************* 3.Rank the employees (EmployeeID) according to their total sales together with their names ?


%%sql 
select sum(p.Price) as Sales
from Employees e 
left join Orders o on e.EmployeeID=o.EmployeeID 
left join OrderDetails od on od.OrderID=o.OrderID
left join Products p on p.ProductID=od.ProductID
group by EmployeeID
order by Sales desc;


# ----------------------------------------------------------------------------------------------------------------


# *****************  4.What are the average prices of orders from Germany by category?


%%sql
select c.CategoryName, avg(p.Price) as Avarage_Price
from OrderDetails od
left join Products p on od.ProductID=p.ProductID
left join Categories c on c.CategoryID=p.CategoryID
left join Orders o on o.OrderID=od.OrderID
left join Customers cd on cd.CustomerID=o.CustomerID
where Country='Germany'
group by c.CategoryID; 


# ----------------------------------------------------------------------------------------------------------------


# *************  5.What are the average prices of orders from Germany or the USA by category?


%%sql
select c.CategoryName, avg(p.Price) as Avarage_Price
from OrderDetails od
left join Products p on od.ProductID=p.ProductID
left join Categories c on c.CategoryID=p.CategoryID
left join Orders o on o.OrderID=od.OrderID
left join Customers cd on cd.CustomerID=o.CustomerID
where Country='Germany' or Country='USA'
group by c.CategoryID; 


# ----------------------------------------------------------------------------------------------------------------


# ************* 6.What is the average price of orders placed in June July August?


%%sql 
select avg(p.Price) as Avarage
from Orders o 
left join OrderDetails od on od.OrderID=o.OrderID
left join Products p on p.ProductID=od.ProductID
where o.OrderDate like '%07%' or o.OrderDate like '%08%' or o.OrderDate like '%09%';


# ----------------------------------------------------------------------------------------------------------------


# ********* 7.Find the maximum quantities of the customers' orders for 1997 and sort them in descending order 
#                             with the names of the customers ********* ?


%%sql
select c.CustomerName,max(p.Price) as Quantity
from Orders o
left join Customers c on c.CustomerID=o.CustomerID
left join OrderDetails od on o.OrderID=od.OrderID
left join Products p on p.ProductID=od.ProductID
where o.OrderDate like '%1997%'
group by CustomerName
order by Quantity desc;


# ********** 8.Rank the employees who received orders with the order year 1997 according to the number of orders received?


%%sql
select e.FirstName,count(e.EmployeeID) as Number_of_Orders
from Orders o
left join Employees e on e.EmployeeID=o.EmployeeID
where o.OrderDate like '%1997%'
group by o.EmployeeID
order by Number_of_Orders desc;

