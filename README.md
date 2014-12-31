# shijian

Python change and time functions

# quick start

Clocks can be created in a straightforward way such as the following:

    alpha = shijian.Clock(name = "alpha")

By default, clocks keep time from their creation time. This behaviour can be disabled using the ```start = False``` Boolean argument. Clocks can be assigned a name or can generate their own unique identifier. Clocks can be stopped easily:

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
print(alpha.startTime())
print(alpha.stopTime())
print(alpha.time())
```

Clocks can also provide a general printout of their characteristics:

```Python
alpha.printout()
```

All clocks are recorded in the shijian list of clocks. Printouts of the clocks are available in two styles: full and statistics. The full style returns the elapsed times of all clocks while the default statistics style returns the mean times of all clocks of the same name.

```Python
shijian.clocks.printout(style = "full")
shijian.clocks.printout()
```

# future

Under consideration are timing decorators.
