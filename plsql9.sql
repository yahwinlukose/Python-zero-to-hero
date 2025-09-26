create or replace function get_square(p_num in number)
return number
is
  v_result number;
BEGIN
  v_result :=p_num*p_num;
  return v_result;
end;
/
set serveroutput on;
BEGIN
    DBMS_OUTPUT.PUT_LINE('square of 9 is:' || get_square(9));
end;
/        
