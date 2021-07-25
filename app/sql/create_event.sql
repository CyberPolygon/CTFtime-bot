insert into events
(
    name,
    date,
    format,
    location,
    weight,
    notes,
    url
)
values
(
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
returning id;