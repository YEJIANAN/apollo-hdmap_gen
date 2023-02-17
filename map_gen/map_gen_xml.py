import xml.etree.ElementTree as ET

root = ET.Element('lane')
id = ET.SubElement(root, 'id', {'id': '1'})
central_curve = ET.SubElement(root, 'central_curve')
segment = ET.SubElement(central_curve, 'segment')
line_segment = ET.SubElement(segment, 'line_segment')
point = ET.SubElement(line_segment, 'point')
x = ET.SubElement(point, 'x')
y = ET.SubElement(point, 'y')

length = ET.SubElement(segment, 'length')

left_broundary = ET.SubElement(root, 'left_broundary')
curve = ET.SubElement(left_broundary, 'curve')
segment = ET.SubElement(curve, 'segment')
line_segment = ET.SubElement(segment, 'line_segment')
point = ET.SubElement(line_segment, 'point')
x = ET.SubElement(point, 'x')
y = ET.SubElement(point, 'y')
length = ET.SubElement(segment, 'length')
boundary_type = ET.SubElement(segment, 'boundary_type')
s = ET.SubElement(boundary_type, 's')
types = ET.SubElement(boundary_type, 'types')

right_broundary = ET.SubElement(root, 'right_broundary')
curve = ET.SubElement(right_broundary, 'curve')
segment = ET.SubElement(curve, 'segment')
line_segment = ET.SubElement(segment, 'line_segment')
point = ET.SubElement(line_segment, 'point')
x = ET.SubElement(point, 'x')
y = ET.SubElement(point, 'y')
length = ET.SubElement(segment, 'length')
boundary_type = ET.SubElement(segment, 'boundary_type')
s = ET.SubElement(boundary_type, 's')
types = ET.SubElement(boundary_type, 'types')

length = ET.SubElement(root, 'length')
speed_limit = ET.SubElement(root, 'speed_limit')
predecessor_id = ET.SubElement(root, 'predecessor_id')
id = ET.SubElement(predecessor_id, 'id')
successor_id = ET.SubElement(root, 'successor_id')
id = ET.SubElement(successor_id, 'id')
left_neighbor_forward_lane_id = ET.SubElement(
    root, ' left_neighbor_forward_lane_id')
id = ET.SubElement(left_neighbor_forward_lane_id, 'id')
right_neighbor_forward_lane_id = ET.SubElement(
    root, 'right_neighbor_forward_lane_id')
id = ET.SubElement(right_neighbor_forward_lane_id, 'id')

type = ET.SubElement(root, 'type')
turn = ET.SubElement(root, 'trun')

left_sample = ET.SubElement(root, 'left_sample ')
s = ET.SubElement(left_sample, 's')
width = ET.SubElement(left_sample, 'width')

right_sample = ET.SubElement(root, 'right_sample')
s = ET.SubElement(right_sample, 's')
width = ET.SubElement(right_sample, 'width')

direction = ET.SubElement(root, 'direction')

root2 = ET.Element('road')
id = ET.SubElement(root2, 'id')
section = ET.SubElement(root2, 'section')
id = ET.SubElement(section, 'id')
lane_id = ET.SubElement(section, 'lane_id')
id = ET.SubElement(lane_id, 'id')


