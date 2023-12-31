import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
  """Класс для вывода игровой информации."""
  
  def __init__(self, ai_game):
    """Инициализирует атрибуты подсчета очков."""
    self.ai_game = ai_game
    self.screen = ai_game.screen
    self.screen_rect = self.screen.get_rect()
    self.settings = ai_game.settings
    self.stats = ai_game.stats

    # Настройки шрифта для вывода счета.
    self.text_color = (30, 30, 30)
    self.font = pygame.font.SysFont(None, 48)
    # Подготовка изображений счетов.
    self.prep_score()
    self.prep_high_score()
    self.prep_level()
    self.prep_ships() 
    self.prep_kill()                                                                                                       
 
  def prep_score(self):
    """Преобразует текущий счет в графическое изображение."""
    rounded_score = round(self.stats.score, -1)
    score_str = f'Счет: {"{:,}".format(rounded_score)}'
    self.score_image = self.font.render(score_str, True,
      self.text_color, self.settings.bg_color)

    # Вывод счета в правой верхней части экрана.
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20

  def show_score(self):
    # Вывод счета на экран
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.screen.blit(self.level_image,self.level_rect)
    self.ships.draw(self.screen)
    self.screen.blit(self.kill_image, self.kill_rect)
    

  def prep_high_score(self):
    """Преобразует рекордный счет в графическое изображение."""
    high_score =round(self.stats.high_score, -1)
    high_score_str = f'Record: {"{:,}".format(high_score)}'
    self.high_score_image = self.font.render(high_score_str, True,
    self.text_color, self.settings.bg_color)

    # Рекорд выравнивается по центру верхней стороны.
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.right = self.screen_rect.right - 20
    self.high_score_rect.bottom = self.screen_rect.bottom / 2  

  def check_high_score(self):
    """Проверяет, появился ли новый рекорд."""
    if self.stats.score > self.stats.high_score:
      self.stats.high_score = self.stats.score
      with open('rezul.txt', 'w') as file_object:
        file_object.write(str(self.stats.score))
      self.prep_high_score()
      self.prep_level()

  def prep_level(self):
    """Преобразует уровень в графическое изображение."""
    level_str = f'Level:  {str(self.stats.level)}'
    self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

    # Уровень выводится под текущим счетом.
    self.level_rect = self.level_image.get_rect()
    self.level_rect.right = self.score_rect.right
    self.level_rect.top = self.score_rect.bottom + 100



  def prep_ships(self):
    """Сообщает количество оставшихся кораблей."""
    self.ships = Group()
    for ship_number in range(self.stats.ships_left):
      ship = Ship(self.ai_game)
      ship.rect.x = self.score_rect.right - ship.rect.width - ship_number * ship.rect.width
      ship.rect.y = self.screen_rect.bottom - ship.rect.height -20
      self.ships.add(ship)

  def prep_kill(self):
    kill_str = f'Kill- {str(self.stats.kill)}'
    self.kill_image = self.font.render(kill_str, True, self.text_color,self.settings.bg_color)

    # вывод результата на экран
    self.kill_rect = self.kill_image.get_rect()
    self.kill_rect.right = self.screen_rect.right - 20
    self.kill_rect.top = self.screen_rect.bottom / 2