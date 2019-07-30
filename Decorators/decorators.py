def do_twice(func):
	def wrapper_do_twice():
		func()
		func()
	return wrapper_do_twice

## -- decorator template for decorating functions with/without arguments
def decorator_with_args(func):
	def wrapper_decorator(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper_decorator


## -- returning values
def decorator_return(func):
	def wrapper_return(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper_return

## -- add function introspection to allow functions
## -- to know their own name and documentation
import functools

def decorator_with_id(func):
	@functools.wraps(func) ## -- this assigns the "identity" (signature, documentation) of the decorated functions
	## -- define decorator as usual
	def wrapper_with_id(*args, **kwargs):
		return func(*args, **kwargs)
	return wrapper_with_id

## -- generic decorator template
def decorator(func):
	@functools.wraps(func)
	def wrapper_decorator(*args, **kwargs):
		## -- do something before
		value = func(*args, **kwargs)
		## -- do something after
		return value
	return wrapper_decorator
