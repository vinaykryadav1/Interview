create database interview;
use interview;

#1 Second Highest Salary
# Write an SQL query to report the second highest salary from the Employee table. If there is no second highest salary, the query should report null
select max(salary) as m_salary from employee where salary < (select max(salary) from employee);

#2 Nth Highest Salary
#Write an SQL query to report the nth highest salary from the Employee table. If there is no nth highest salary, the query should report null.
with n_Hsalary as (
	select *, rank() over(order by salary desc) as ranked from employee
)select id,salary,ranked from n_Hsalary where ranked= 3;

#3 Consecutive Numbers
# Write an SQL query to find all numbers that appear at least three times consecutively.
with sub as (
	select num,lag(num,1) over (order by Id) as prev_1 , lag(num,2) over (order by Id) as prev_2 from logse
)select distinct num from sub where num = prev_1 and num = prev_2;

#4 Employees Earning More Than Their Managers
#Write an SQL query to find the employees who earn more than their managers.
select e.name, e.salary, m.name, m.salary from employee e join employee m on e.manager_id = m.id where e.salary>m.salary;

#5 Duplicate Emails
#Write an SQL query to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
select email,count(*) as counts from person group by email having count(*) > 1;

#6 Delete Duplicate Emails
with email_count as (
	select *, row_number() over(partition by email)as e_count from person
)delete from person where personId in (select personId from email_count where e_count = 2 );

#7 Customers Who Never Order
#Write an SQL query to report all customers who never order anything.
select customerId,name from customers where customerId not in (select customerId from orders);

#8 Department Highest Salary
#Write an SQL query to find employees who have the highest salary in each of the departments. (manager_id = departmentID)
select e.manager_id ,d.name,max(e.salary) as m_salary from employee e join department d on e.manager_id = d.id group by e.manager_id;

#9 Rising Temperature
#Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates(yesterday).
select t1.recordDate from weather t1 join weather t2 on datediff(t1.recordDate,t2.recordDate) = 1 where t1.temperature > t2.temperature ;

#10 Trips and Users
#The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on thatday.Write a SQL query to find the cancellation rate of requests with unbanned users (both client anddriver must not be banned) each day between "2013-10-01" and "2013-10-03". RoundCancellation Rate to two decimal points.
select request_at ,round(sum(case when status in ('cancelled_by_driver', 'cancelled_by_client') then 1 else 0 end) / count(*),2) as cancellation_rate from trips t 
join users c on t.client_id = c.users_id AND c.banned = 'No' join users d on t.driver_id = d.users_id AND d.banned = 'No' where request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY request_at ORDER BY request_at;




