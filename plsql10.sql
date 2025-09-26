create or replace function format_name(p_name in varchar2)
return varchar2
is
BEGIN
    return UPPER(p_name);
END;
/
set serveroutput on;
BEGIN
    DBMS_OUTPUT.PUT_LINE('formatted number:' || format_name('John Doe'));
END;
/        