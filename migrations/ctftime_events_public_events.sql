create table events
(
    id       serial      not null
        constraint events_pk
            primary key,
    name     varchar(64) not null,
    date     varchar(80) not null,
    format   varchar(20) not null,
    location varchar(64) not null,
    weight   double precision default 0,
    notes    varchar(80),
    url      varchar(64) not null
);

alter table events
    owner to postgres;

create unique index events_id_uindex
    on events (id);

create unique index events_name_uindex
    on events (name);

create unique index events_url_uindex
    on events (url);
