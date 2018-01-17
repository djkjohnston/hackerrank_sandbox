--https://www.hackerrank.com/challenges/occupations/problem

SET 
	@doctor_row=0, 
	@professor_row=0, 
	@singer_row=0, 
	@actor_row=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@doctor_row:=@doctor_row+1)
            when Occupation='Professor' then (@professor_row:=@professor_row+1)
            when Occupation='Singer' then (@singer_row:=@singer_row+1)
            when Occupation='Actor' then (@actor_row:=@actor_row+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
) Temp
group by RowNumber