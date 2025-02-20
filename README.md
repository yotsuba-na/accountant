# Accountant
Logging the fact and scheduled spend to/from a wallet

### Todo
```
WebApp
  if not is_logged:
    redirect(login)
  redirect(main)
```
- [ ] / - summary, REST calls
- [ ] /auth
  - [ ] /login
  - [ ] /register
  - [ ] /reset
  - [ ] /confirm
- [x] /user
  - [x] Add wallet
  - [ ] Add currency
- [ ] /transaction
  - [ ] Add transaction
    - [x] Regular
    - [ ] Schedule
    - [ ] Transfer

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
+------+----------+
| date | All/Only | - All data, Only for this $date
+------+----------+

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
```SQL
-- transaction
	id 		INTEGER PRIMARY KEY AUTOINCREMENT
	owner_id	INTEGER FOREIGN KEY @user
	parent_id	INTEGER FOREIGN KEY @transaction
	title		VARCHAR (50) NOT NULL
	status		VARCHAR (10) NOT NULL {'planned', 'fact'}
	type_id		INTEGER FOREIGN KEY @transaction_type
	function_id	INTEGER FOREIGN KEY @transaction_function
	wallet_id	INTEGER FOREIGN KEY @wallet
	currency_id	INTEGER FOREIGN KEY @currency
	value		DECIMAL NOT NULL
	created_at	DATETIME
	updated_at	DATETIME

	-- transaction_type
		id	INTEGER PRIMARY KEY AUTOINCREMENT
		type	VARCHAR (10) NOT NULL {'regular', 'schedule', 'transfer'}

	-- transactin_function
		id	INTEGER PRIMARY KEY AUTOINCREMENT
		func	VARCHAR (10) NOT NULL {'increment', 'decrement'}

-- transaction_transfer
	id		INTEGER PRIMARY KEY AUTOINCREMENT
	owner_id	INTEGER FOREIGN KEY @user
	transaction_id	INTEGER FOREIGN KEY @transaction
	transfer_from	INTEGER FOREIGN KEY @wallet
	transfer_to	INTEGER FOREIGN KEY @wallet
	currency_id	INTEGER FOREIGN KEY @currency
	value		DECIMAL NOT NULL

-- user
	id		INTEGER PRIMARY KEY AUTOINCREMENT
	fullname	VARCHAR (50) NOT NULL
	currency_id	INTEGER FOREIGN KEY @currency

-- currency
	id		INTEGER PRIMARY KEY AUTOINCREMENT
	currency	VARCHAR (10) NOT NULL
	value		DECIMAL NOT NULL
	created_at	DATETIME
	updated_at	DATETIME

-- wallet
	id		INTEGER PRIMARY KEY AUTOINCREMENT
	title		VARCHAR (50)
	owner_id	INTEGER FOREIGN KEY @user
	balance		DECIMAL NOT NULL
	currency_id	INTEGER FOREIGN KEY @currency
	type_id		INTEGER FOREIGN KEY @wallet_type

	-- wallet_type
		id	INTEGER PRIMARY KEY AUTOINCREMENT
		type	VARCHAR (10) {'linked', 'shared', 'temporary'}

-- filters
	id		INTEGER PRIMARY KEY AUTOINCREMENT
	owner_id	INTEGER FOREIGN KEY @user
	obj_name	VARCHAR (10) {'user', 'currency'}
	obj_ids		TEXT    NOT NULL	-- TODO: OneToMany Relation
```
