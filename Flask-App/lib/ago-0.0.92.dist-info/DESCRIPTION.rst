What are human readable timedeltas? 
===============================================

ago.py makes customizable human readable timedeltas, for example:

Testing past tense::

 Russell commented 1 year, 127 days, 16 hours ago
 You replied 1 year, 127 days ago

Testing future tense::

 Program will shutdown in 2 days, 3 hours, 27 minutes
 Job will run 2 days, 3 hours from now


How to install
===================

There are a number of ways to install this package.

You could run this ad hoc command::

 pip install ago

or specify *ago* under the *setup_requires* list within your
*setuptools*-compatible project's *setup.py* file.


How to use
==================

The ago module comes with three functions: 

#. human
#. delta2dict
#. get_delta_from_subject

You really only need to worry about *human*.

Here are all the available arguments and defaults::

 human(subject, precision=2, past_tense='{} ago', future_tense='in {}', abbreviate=False):

subject
 a datetime, timedelta, or timestamp (integer/float) object to become human readable

precision (default 2):
 the desired amount of unit precision

past_tense (default '{} ago'):
 the format string used for a past timedelta

future_tense (default 'in {}'):
 the format string used for a future timedelta

abbreviate (default False):
 boolean to abbreviate units

Here is an example on how to use *human*::

 from ago import human
 from ago import delta2dict

 from datetime import datetime
 from datetime import timedelta

 # pretend this was stored in database
 db_date = datetime(year=2010, month=5, day=4, hour=6, minute=54, second=33, microsecond=4000)

 # to find out how long ago, use the human function
 print 'Created ' + human( db_date )

 # optionally pass a precision
 print 'Created ' + human( db_date, 3 )
 print 'Created ' + human( db_date, 6 )

We also support future dates and times::

 PRESENT = datetime.now()
 PAST = PRESENT - timedelta( 492, 58711, 45 ) # days, secs, ms
 FUTURE = PRESENT + timedelta( 2, 12447, 963 ) # days, secs, ms

 print human( FUTURE )

Example past_tense and future_tense keyword arguments::

 output1 = human( PAST,
   past_tense = 'titanic sunk {0} ago',
   future_tense = 'titanic will sink in {0} from now'
 )

 output2 = human( FUTURE,
   past_tense = 'titanic sunk {0} ago',
   future_tense = 'titanic will sink in {0} from now'
 )

 print output1
 # titanic sunk 1 year, 127 days ago
 print output2
 # titanic will sink in 2 days, 3 hours from now


Need more examples?
==========================

You should look at test_ago.py


How do I thank you?
==========================

You should follow me on twitter http://twitter.com/russellbal


License
=========================

Public Domain


Public Revision Control
==============================

https://bitbucket.org/russellballestrini/ago


