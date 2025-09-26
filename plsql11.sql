create or replace function get_salary(p_emp_id in number)
return number
is
    v_salary number;
BEGIN
    select salary into v_salary from employees where employee_id = p_emp_id;    
    return v_salary;
exception
    when no_data_found then
        return 0;
end;
/
set serveroutput on;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Salary is: ' || get_salary(101));
END;    
/