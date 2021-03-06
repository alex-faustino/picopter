# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from picopter/Interface.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class Interface(genpy.Message):
  _md5sum = "d48df5094a97ac2271d10199017658de"
  _type = "picopter/Interface"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool is_calibrated
bool arm_esc
bool flight_mode
bool stop_motors
bool shutdown
"""
  __slots__ = ['is_calibrated','arm_esc','flight_mode','stop_motors','shutdown']
  _slot_types = ['bool','bool','bool','bool','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       is_calibrated,arm_esc,flight_mode,stop_motors,shutdown

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Interface, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.is_calibrated is None:
        self.is_calibrated = False
      if self.arm_esc is None:
        self.arm_esc = False
      if self.flight_mode is None:
        self.flight_mode = False
      if self.stop_motors is None:
        self.stop_motors = False
      if self.shutdown is None:
        self.shutdown = False
    else:
      self.is_calibrated = False
      self.arm_esc = False
      self.flight_mode = False
      self.stop_motors = False
      self.shutdown = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.is_calibrated, _x.arm_esc, _x.flight_mode, _x.stop_motors, _x.shutdown))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.is_calibrated, _x.arm_esc, _x.flight_mode, _x.stop_motors, _x.shutdown,) = _get_struct_5B().unpack(str[start:end])
      self.is_calibrated = bool(self.is_calibrated)
      self.arm_esc = bool(self.arm_esc)
      self.flight_mode = bool(self.flight_mode)
      self.stop_motors = bool(self.stop_motors)
      self.shutdown = bool(self.shutdown)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5B().pack(_x.is_calibrated, _x.arm_esc, _x.flight_mode, _x.stop_motors, _x.shutdown))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 5
      (_x.is_calibrated, _x.arm_esc, _x.flight_mode, _x.stop_motors, _x.shutdown,) = _get_struct_5B().unpack(str[start:end])
      self.is_calibrated = bool(self.is_calibrated)
      self.arm_esc = bool(self.arm_esc)
      self.flight_mode = bool(self.flight_mode)
      self.stop_motors = bool(self.stop_motors)
      self.shutdown = bool(self.shutdown)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5B = None
def _get_struct_5B():
    global _struct_5B
    if _struct_5B is None:
        _struct_5B = struct.Struct("<5B")
    return _struct_5B
