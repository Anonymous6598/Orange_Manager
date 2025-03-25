import g4f

class LargeLanguageModel:
    def ResponseFromAI(self, prompt):
        self.user_query = [{f"role": f"user", f"content": prompt}]
        
        self.response = g4f.ChatCompletion.create(model=f"gpt-4o", messages=self.user_query)

        return self.response