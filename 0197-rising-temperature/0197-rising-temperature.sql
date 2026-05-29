select w1.id
from Weather w1
where w1.temperature>(
    select w2.temperature
    from Weather w2
    where w1.recordDate=w2.recordDate+ interval 1 day
);