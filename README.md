# Accountant
Logging the income and outcome money

#### Routes
```
WebApp
  if not is_logged:
    redirect(login)
  redirect(main)
```
- [ ] / - widgets, summary, navbar with data and quick links
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [ ] /finance
  - [ ] /user/<user_id>
- [ ] /crud - main crud page for all users to vote ?!
  - [ ] /user/<user_id>
- [ ] /user/<user_id>

#### Main
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
