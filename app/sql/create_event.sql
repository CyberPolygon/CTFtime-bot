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
    {name},
    {date},
    {format},
    {location},
    {weight},
    {notes},
    {url}
)
returning id;