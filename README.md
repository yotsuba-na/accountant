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
+---------+    +--------------------------------------------+    +-----------------------+
| $filter |    | $summary_filtered (c for c in $currencies) |    | $summary_not_filtered |
+---------+    +--------------------------------------------+    +-----------------------+


@block body
+---------+    +--------------------------------------------+    +-----------------------+
| $user_N |    | $scheduled_income                          |    | in/outcome $log       |
|         |    | ------------------------------------------ |    |                       |
+---------+    | $scheduled_outcome                         |    +-----------------------+
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
| @table.Currency | id  | Currency | Value | Updated_at |
| :-------------: | :-: | :------: | :---: | :--------: |

| @table.Users | id  | NickName | CurrencyID |
| :----------: | :-: | :------: | :------------: |

<hr />

| @table.Wallet | id  | Uid | Balance | Shared |
| :-----------: | :-: | :-: | :-----: | :----: |

<hr />

| @table.ScheduleCode | id  | Uid | Code |
| :-----------------: | :-: | :-: | :--: |

| @table.FuncCode | id  | Uid | Code |
| :-------------: | :-: | :-: | :--: |

| @table.Schedule | id  | Uid | Title | ScheduleCodeID | FuncCodeID | Value | Wid |
| :-------------: | :-: | :-: | :---: | :------------: | :--------: | :---: | :-: |

<hr />

| @table.Filters | id  | Uid | ObjName | ObjIDs |
| :------------: | :-: | :-: | :-----: | :----: |

<hr />

| @table.TodoCurrency | id  | Tid | CurrencyID | Value |
| :-----------------: | :-: | :-: | :--------: | :---: |

| @table.Todo | id  | Uid | Title | State | TodoCurrencyID | Value | Created_at |
| :---------: | :-: | :-: | :---: | :---: | :------------: | :---: | :------: |

| @table.TodoItem | id  | Uid | Tid | Title | State | TodoCurrencyID | Value | Created_at |
| :-------------: | :-: | :-: | :-: | :---: | :---: | :------------: | :---: | :------: |
