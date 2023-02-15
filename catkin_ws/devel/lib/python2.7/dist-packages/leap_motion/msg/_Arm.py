# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from leap_motion/Arm.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class Arm(genpy.Message):
  _md5sum = "b93012a87e6395b9975695d8d7a942db"
  _type = "leap_motion/Arm"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header

# The position and orientation of the elbow. 
geometry_msgs/Pose elbow

# The position and orientation of the wrist. 
geometry_msgs/Pose wrist

# The midpoint of the forearm. 
float32[] center

# The direction vector of the forearm
geometry_msgs/Vector3 direction

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','elbow','wrist','center','direction']
  _slot_types = ['std_msgs/Header','geometry_msgs/Pose','geometry_msgs/Pose','float32[]','geometry_msgs/Vector3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,elbow,wrist,center,direction

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(Arm, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.elbow is None:
        self.elbow = geometry_msgs.msg.Pose()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Pose()
      if self.center is None:
        self.center = []
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
    else:
      self.header = std_msgs.msg.Header()
      self.elbow = geometry_msgs.msg.Pose()
      self.wrist = geometry_msgs.msg.Pose()
      self.center = []
      self.direction = geometry_msgs.msg.Vector3()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.elbow.position.x, _x.elbow.position.y, _x.elbow.position.z, _x.elbow.orientation.x, _x.elbow.orientation.y, _x.elbow.orientation.z, _x.elbow.orientation.w, _x.wrist.position.x, _x.wrist.position.y, _x.wrist.position.z, _x.wrist.orientation.x, _x.wrist.orientation.y, _x.wrist.orientation.z, _x.wrist.orientation.w))
      length = len(self.center)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.Struct(pattern).pack(*self.center))
      _x = self
      buff.write(_get_struct_3d().pack(_x.direction.x, _x.direction.y, _x.direction.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.elbow is None:
        self.elbow = geometry_msgs.msg.Pose()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Pose()
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.elbow.position.x, _x.elbow.position.y, _x.elbow.position.z, _x.elbow.orientation.x, _x.elbow.orientation.y, _x.elbow.orientation.z, _x.elbow.orientation.w, _x.wrist.position.x, _x.wrist.position.y, _x.wrist.position.z, _x.wrist.orientation.x, _x.wrist.orientation.y, _x.wrist.orientation.z, _x.wrist.orientation.w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.center = s.unpack(str[start:end])
      _x = self
      start = end
      end += 24
      (_x.direction.x, _x.direction.y, _x.direction.z,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_14d().pack(_x.elbow.position.x, _x.elbow.position.y, _x.elbow.position.z, _x.elbow.orientation.x, _x.elbow.orientation.y, _x.elbow.orientation.z, _x.elbow.orientation.w, _x.wrist.position.x, _x.wrist.position.y, _x.wrist.position.z, _x.wrist.orientation.x, _x.wrist.orientation.y, _x.wrist.orientation.z, _x.wrist.orientation.w))
      length = len(self.center)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.center.tostring())
      _x = self
      buff.write(_get_struct_3d().pack(_x.direction.x, _x.direction.y, _x.direction.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.elbow is None:
        self.elbow = geometry_msgs.msg.Pose()
      if self.wrist is None:
        self.wrist = geometry_msgs.msg.Pose()
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 112
      (_x.elbow.position.x, _x.elbow.position.y, _x.elbow.position.z, _x.elbow.orientation.x, _x.elbow.orientation.y, _x.elbow.orientation.z, _x.elbow.orientation.w, _x.wrist.position.x, _x.wrist.position.y, _x.wrist.position.z, _x.wrist.orientation.x, _x.wrist.orientation.y, _x.wrist.orientation.z, _x.wrist.orientation.w,) = _get_struct_14d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.center = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 24
      (_x.direction.x, _x.direction.y, _x.direction.z,) = _get_struct_3d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_14d = None
def _get_struct_14d():
    global _struct_14d
    if _struct_14d is None:
        _struct_14d = struct.Struct("<14d")
    return _struct_14d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
