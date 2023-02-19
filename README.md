# Accountant
Logging the fact and scheduled spend to/from a wallet

### Todo
```
WebApp
  if not is_logged:
    redirect(login)
  redirect(main)
```
- [ ] / - widgets, summary, navbar with data and quick links
  - [ ] add currency
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [ ] /user
  - [ ] Add wallet
  - [ ] Add schedule
  - [ ] Add todo

### Main Page
```
@block nav
+---------+    +-------------+------+-----+------+----------+    +-----------------------+
| $filter |    | $currencies < *[@] | $dd < *[@] | $SubForm |    | $summary_not_filtered |
+---------+    +-------------+------+-----+------+----------+    +-----------------------+


@block body
+---------+    +--------------------------------------------+    +-----------------------+
| $user_N |    | $scheduled_income  [@]                     |    | in/outcome $log       |
|         |    | ------------------------------------------ |    |                       |
+---------+    | $scheduled_outcome [@]                     |    +-----------------------+
 %scroll       +--------------------------------------------+     %scroll


               +---------------+ +--------------------------+
               | $todo - title | | $todo - body             |
               +---------------+ +--------------------------+
                % scroll


$filter
+-----------+---------+
| date_from | date_to | - default this.month
+-----------+---------+

$c - currency

$dd - drop down (selection)

$subForm - form to submit a data

$summary_? (in/out)
+---------+
| +in     | - $filtered      = after filter apply
| -out $c | - $not_filtered  = from start
+---------+

$user_N - { float: left }
+----------------+
| [] User_name   | - $checkbox as a filter
|    +---------+ |
|    | -in     | | - $not_filtered
|    | +out $c | |
|    +---------+ |
+----------------+

$scheduled (income/outcome) - { justify-content: center }
+----------------+
| [] title       |
|    +---------+ |
|    | -in  $c | |
|    +---------+ |
+----------------+

$log - { float: right }
+----+---------------+---------+----------+
| id | in/outcome $c | $user_N | datetime |
+----+---------------+---------+----------+

$todo - title
+----+--------+
| id | $title |
+----+--------+

$todo - body
+---------------+
| [] item title |
|---------------|
| $actions      | - $complete, $delete, $select
+---------------+

%scroll - scrollable data
```

### DB Tables
| @table.currency | id  | currency | value | updated_at |
| :-------------: | :-: | :------: | :---: | :--------: |
|                 |  1  |    USD   |  0.45 | timestamp  |
|                 |  2  |    JPY   |  0.20 | timestamp  |

| @table.users | id  | nickname | currency_id |
| :----------: | :-: | :------: | :---------: |
|              |  1  |  noName  |      1      |

<hr />

| @table.wallet | id  | u_id | balance | shared |
| :-----------: | :-: | :--: | :-----: | :----: |
|               |  1  |  1   |  32.49  | false  |

<hr />

| @table.schedule_code | id  | code |
| :------------------: | :-: | :--: |
|                      |  1  |   d  |
|                      |  2  |   m  |

| @table.func_code | id  | u_id | code |
| :--------------: | :-: | :--: | :--: |
|                  |  1  |  1   | inc  |

| @table.schedule | id  | u_id | title | schedule_code_id | schedule_repeat | func_code_id | value | w_id |
| :-------------: | :-: | :--: | :---: | :--------------: | :-------------: | :----------: | :---: | :--: |
|                 |  1  |  1   | daily |         1        |        *        |       1      |  0.5  |  1   |

<hr />

| @table.filters | id  | u_id | obj_name | obj_ids |
| :------------: | :-: | :--: | :------: | :-----: |
|                |  1  |  1   |  Users   | 1,2,3   |

<hr />

| @table.todo_currency | id  | t_id | currency_id | Value |
| :------------------: | :-: | :--: | :---------: | :---: |
|                      |  1  |   1  |      1      | 0.40  |

| @table.todo | id  | u_id | title | State | todo_currency_id | value | created_at |
| :---------: | :-: | :--: | :---: | :---: | :--------------: | :---: | :--------: |
|             |  1  |  1   | my td |   0   |         1        | 10.00 | timestamp  |

| @table.todo_item | id  | u_id | t_id | title | state | todo_currency_id | value | created_at |
| :--------------: | :-: | :--: | :--: | :---: | :---: | :--------------: | :---: | :--------: |
|                  |  1  |  1   |  1   | my t  |   0   |         1        |  5.0  | timestamp  |
|                  |  2  |  1   |  1   | my d  |   0   |         1        |  5.0  | timestamp  |
