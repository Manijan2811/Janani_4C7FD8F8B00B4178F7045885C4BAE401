#cricket

class batsman:
  def __init__(self):
    self.strike_rate=0.0
    self.total_runs=0
    self.highest_score=0
    self.batting_rate=0
  def get_bat(self,a,b,c,d):
    self.strike_rate=a
    self.total_runs=b
    self.highest_score=c
    self.batting_rate=d
  def disp_bat(self):
    print("THE BATTING MAN")
    print("Strike_rate:",self.strike_rate)
    print("Total_runs",self.total_runs)
    print("Highest_score",self.highest_score)
    print("Batting_rates",self.batting_rate)
class bowler:
  def __init__(self):
    self.wickets=0
    self.economy=0.0
    self.hattricks=0
    self.bowling_rank=0
  def get_bowl(self,e,f,g,h):
    self.wickets=e
    self.economy=f
    self.hattricks=g
    self.bowling_rank=h
  def disp_bowl(self):
    print("THE BOWLER")
    print("The wickets:",self.wickets)
    print("Economy:",self.economy)
    print("Hattricks:",self.hattricks)
    print("Bowling_rank:",self.bowling_rank)
class allrounder(batsman,bowler):
  def __init__(self):
    batsman.__init__(self)
    bowler.__init__(self)
    self.allrounder_rank=0
  def get_all(self,a,b,c,d,e,f,g,h,i):
    batsman.get_bat(self,a,b,c,d)
    bowler.get_bowl(self,e,f,g,h)
    self.allrounder_rank=i
  def disp_all(self):
    print("ALL ROUNDER")
    print("Allrounder_rank:",self.allrounder_rank)
    self.disp_bat()
    self.disp_bowl()
Mani=allrounder()
Mani.get_all(89.7,3024,96,67,101,5.67,4,34,57)
Mani.disp_all()