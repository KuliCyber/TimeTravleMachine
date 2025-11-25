import uuid
import datetime

class ParadoxSolver:
    def __init__(self):
        self.reality_branches = {}
        self.paradox_resolutions = 0
        self.timeline_integrity = 100
        
    def create_reality_branch(self, original_data, changes):
        branch_id = str(uuid.uuid4())[:8]
        new_reality = original_data.copy()
        new_reality.update(changes)
        new_reality['branch_id'] = branch_id
        new_reality['created_at'] = datetime.datetime.now()
        
        self.reality_branches[branch_id] = new_reality
        return branch_id
    
    def handle_grandfather_paradox(self, traveler_actions):
        if traveler_actions.get('prevents_own_birth'):
            branch_id = self.create_reality_branch(
                {'paradox_type': 'grandfather'},
                {'traveler_exists': False, 'resolution': 'quantum_branch'}
            )
            self.paradox_resolutions += 1
            return branch_id
        return "prime_timeline_stable"
    
    def handle_butterfly_effect(self, changes):
        if len(changes) > 10:
            self.timeline_integrity -= 5
            branch_id = self.create_reality_branch(
                {'integrity_warning': True},
                changes
            )
            return branch_id
        return "changes_minor"
    
    def get_reality_map(self):
        return {
            'total_branches': len(self.reality_branches),
            'paradoxes_resolved': self.paradox_resolutions,
            'timeline_integrity': self.timeline_integrity,
            'branches': list(self.reality_branches.keys())
      }
