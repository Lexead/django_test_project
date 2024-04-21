# The startup process and SQL query for test project

## Step 1

```bash
docker-compose build # build image
```

## Step 2

```bash
docker-compose run web python manage.py migrate # apply migrations in Django
```

## Step 3

```bash
docker-compose up --build # re-build image and up container
```

## SQL query (tested on a local pgAdmin)

```sql
SELECT
    u.id,
    u.email,
    COUNT(l.id) AS links,
    SUM(case when l.type  = 'website' then 1 else 0 end) as websites,
    SUM(case when l.type  = 'article' then 1 else 0 end) as articles,
    SUM(case when l.type  = 'book' then 1 else 0 end) as books,
    SUM(case when l.type  = 'music' then 1 else 0 end) as musics,
    SUM(case when l.type  = 'video' then 1 else 0 end) as videos
FROM
    auth_user u
JOIN
    links_link l ON u.id = l.user_id
GROUP BY
    u.id
ORDER BY
    links DESC, u.date_joined
LIMIT 10;
```