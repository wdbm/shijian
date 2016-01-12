# shijian

Python change and time functions

# usage

## time expressions

Function `style_datetime_object` accepts a `datetime` object and returns a string representation of a time. The default style is "YYYY-MM-DDTHHMMSS" and it can be changed by argument. Styles available are as follows:

|**time representation** |**comment**                              |
|------------------------|-----------------------------------------|
|YYYY-MM-DDTHHMMSSZ      |filename safe (default)                  |
|YYYY-MM-DDTHHMMSSMMMMMMZ|microseconds                             |
|YYYY-MM-DD HH:MM:SS UTC |elegant                                  |
|UNIX time S.SSSSSS      |UNIX time in seconds with second fraction|
|UNIX time S             |UNIX time in seconds rounded             |

Functions `time_UTC` and `time_UNIX` are sorts of special cases of function `style_datetime_object` which return representations of the current time (as opposed to any specified datetime object) in a style. For `time_UTC`, the default style is "YYYY-MM-DDTHHMMSS" and for `time_UNIX`, the default style is "UNIX time S" and these styles can be changed by argument.

```Python
>>> shijian.time_UTC()
'2015-01-05T092125Z'
>>> shijian.time_UNIX()
1420449720
```

## unique identifiers

Function `propose_filename` proposes a safe filename. It can accept a filename suggestion or, by default, can generate its own filename suggestion, a time expression returned by function `time_UTC`. Filename suggestions are tested and then proposed if they meet test conditions. The default condition is to not overwrite existing files and to append an underscore followed by an integer in order to meet this condition.

```Python
>python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import shijian
>>> shijian.propose_filename()
'2015-01-05T092319Z'
>>> shijian.propose_filename(filename = "data.pkl")
'data.pkl'
>>> 
>touch data.pkl
>python
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import shijian
>>> shijian.propose_filename(filename = "data.pkl")
'data_1.pkl'
```

Function `UID` returns a 128 bit integer unique identifier in hexadecimal with dashes in accordance with [RFC 4122 UUID version 4](http://tools.ietf.org/html/rfc4122.html).

```Python
>>> shijian.UID()
'91df3b90-285c-4f22-8ced-a154b3b5b09b'
>>> shijian.UID()
'169bde88-2be2-4b46-bf2d-5bb7aee85658'
```

Function `unique_number` returns an integer that does not exist in a global list of integers recorded by the function.

```Python
>>> shijian.unique_number()
1
>>> shijian.unique_number()
2
```

Function `unique_3_digit_number` returns an integer of 3 significant figures that does not exist in a global list of integers of 3 significant figures recorded by the function.

```Python
>>> shijian.unique_3_digit_number()
100
>>> shijian.unique_3_digit_number()
101
```

## clocks

Clocks can be created in a straightforward way such as the following:

    alpha = shijian.Clock(name = "alpha")

By default, clocks keep time from their creation time. This behaviour can be disabled using Boolean argument `start = False`. Clocks can be assigned a name or can generate their own unique identifier. Clocks can be stopped easily:

```Python
beta.stop()
```

and can be started easily:

```Python
alpha.start()
```

Clocks can report on their characteristics in ways such as the following:

```Python
print(alpha.name())
print(alpha.start_time())
print(alpha.stop_time())
print(alpha.time())
```

Clocks can also provide a general printout of their characteristics:

```Python
alpha.printout()
```

All clocks are recorded in the shijian list of clocks. Printouts of clocks are available in two styles: full and statistics. The style "full" returns the elapsed times of all clocks while the default style "statistics" returns the mean times of all clocks of the same name.

```Python
shijian.clocks.printout(style = "full")
shijian.clocks.printout()
```

## filename sequences

The function `natural_sort` naturally sorts a list. The function `find_file_sequences`, for which a directory and file extension can be specified, returns a naturally-sorted list of filenames that are in a sequence or returns a dictionary of lists of filenames that are in a sequence. For example, a list something like the following could be returned:

```Bash
['image-000001.png', 'image-000002.png', 'image-000003.png', 'image-000004.png', 'image-000005.png']
```
