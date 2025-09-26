DECLARE
 cursor c1 is select sname,marks from student where marks>=80;
 rec1 c1%rowtype;
 BEGIN
    for rec1 in c1 LOOP
         DBMS_OUTPUT.PUT_LINE(rec1.sname||' '||rec1.marks);
    end loop;
end;      
/   