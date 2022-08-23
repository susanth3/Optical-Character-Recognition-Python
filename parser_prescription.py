from parser_generic import MedicalDocParser
import re

class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return {
            'patient_name': self.get_field('patient_name'),
            'patient_address' : self.get_field('patient_address'),
            'Medicines prescribed' : self.get_field('medicines'),
            'Usage directions' : self.get_field('directions'),
            'Refill if any' : self.get_field('refills')
        }

    def get_field(self, field_name):
        pattern_dict = {
            'patient_name': {'pattern': 'Name:(.*)Date', 'flags': 0},
            'patient_address': {'pattern': 'Address:(.*)\n', 'flags': 0},
            'medicines': {'pattern': 'Address[^\n]*(.*)Directions', 'flags': re.DOTALL},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'refills': {'pattern': 'Refill:(.*)times', 'flags': 0},
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object['flags'])
            if len(matches) > 0:
                return matches[0].strip()


