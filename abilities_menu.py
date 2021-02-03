import pygame


class AbilityMenu:

	def __init__(self, screen):

		self.screen = screen
		self.background = pygame.image.load("ressource/Background/background_menu.jpg")

		self.button_exit = pygame.image.load("ressource/Menu Boutons/ExitWhite.gif")
		self.button_exit_black = pygame.image.load("ressource/Menu Boutons/ExitBlack.gif")
		self.button_exit_rect = self.button_exit.get_rect()
		self.button_exit_rect.x, self.button_exit_rect.y = 25, 25

		self.image_ability1 = pygame.Surface((200, 200))
		self.image_ability1.fill((255, 0, 0))
		self.rect1 = self.image_ability1.get_rect()
		self.rect1.center = 250, 300

		self.image_ability2 = pygame.Surface((200, 200))
		self.image_ability2.fill((0, 0, 255))
		self.rect2 = self.image_ability2.get_rect()
		self.rect2.center = 250, 600

		self.image_ability3 = pygame.Surface((200, 200))
		self.image_ability3.fill((255, 255, 255))
		self.rect3 = self.image_ability3.get_rect()
		self.rect3.center = 250, 900

		self.shining_surf = [pygame.Surface((700, 220)),
							 pygame.Surface((700, 220)),
							 pygame.Surface((700, 220))]
		self.shining_surf_rect = [i.get_rect() for i in self.shining_surf]

		for i in range(len(self.shining_surf)):
			self.shining_surf_rect[i].left = 140
			self.shining_surf_rect[i].y = 300*i + 190
			self.shining_surf[i].set_alpha(128)
			self.shining_surf[i].fill((255, 255, 255))

		# all frames of a video are stocked there
		self.cw_frames = [pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_000_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_001_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_002_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_003_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_004_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_005_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_006_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_007_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_008_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_009_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_010_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_011_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_012_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_013_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_014_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_015_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_016_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_017_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_018_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_019_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_020_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_021_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_022_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_023_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_024_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_025_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_026_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_027_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_028_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_029_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_030_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_031_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_032_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_033_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_034_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_035_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_036_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_037_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_038_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_039_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_040_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_041_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_042_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_043_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_044_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_045_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_046_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_047_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_048_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_049_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_050_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_051_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_052_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_053_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_054_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_055_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_056_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_057_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_058_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_059_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_060_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_061_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_062_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_063_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_064_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_065_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_066_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_067_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_068_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_069_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_070_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_071_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_072_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_073_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_074_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_075_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_076_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_077_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_078_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_079_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_080_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_081_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_082_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_083_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_084_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_085_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_086_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_087_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_088_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_089_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_090_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_091_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_092_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_093_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_094_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_095_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_096_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_097_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_098_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_099_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_100_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_101_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_102_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_103_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_104_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_105_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Chockwave_frames/frame_106_delay-0.03s.gif")]
		self.index_video_cw = 0
		self.current_image_cw = self.cw_frames[self.index_video_cw]
		self.frame_rect_cw = self.cw_frames[self.index_video_cw].get_rect()

		pygame.draw.rect(self.screen, (0, 255, 0), [960, 530, 400, 20])
		pygame.display.flip()

		self.sh_frames = [pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_000_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_001_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_002_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_003_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_004_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_005_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_006_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_007_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_008_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_009_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_010_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_011_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_012_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_013_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_014_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_015_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_016_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_017_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_018_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_019_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_020_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_021_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_022_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_023_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_024_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_025_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_026_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_027_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_028_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_029_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_030_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_031_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_032_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_033_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_034_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_035_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_036_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_037_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_038_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_039_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_040_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_041_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_042_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_043_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_044_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_045_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_046_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_047_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_048_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_049_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_050_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_051_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_052_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_053_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_054_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_055_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_056_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_057_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_058_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_059_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_060_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_061_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_062_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_063_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_064_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_065_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_066_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_067_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_068_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_069_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_070_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_071_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_072_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_073_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_074_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_075_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_076_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_077_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_078_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_079_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_080_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_081_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_082_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_083_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_084_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_085_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_086_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_087_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_088_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_089_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_090_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_091_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_092_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_093_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_094_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_095_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_096_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_097_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_098_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_099_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_100_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_101_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_102_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_103_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_104_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_105_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_106_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_107_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_108_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_109_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_110_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_111_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_112_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_113_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_114_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_115_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_116_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_117_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_118_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_119_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_120_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_121_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_122_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_123_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_124_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_125_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_126_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_127_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_128_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_129_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_130_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_131_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_132_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_133_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_134_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_135_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_136_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_137_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_138_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_139_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_140_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_141_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_142_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_143_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_144_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_145_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_146_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_147_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_148_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_149_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_150_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_151_delay-0.04s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_152_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_153_delay-0.03s.gif"),
						  pygame.image.load("ressource/Vidéos abilités/Shield_frames/frame_154_delay-0.03s.gif")]

		self.index_video_sh = 0
		self.current_image_sh = self.sh_frames[self.index_video_sh]
		self.frame_rect_sh = self.sh_frames[self.index_video_sh].get_rect()

		pygame.draw.rect(self.screen, (0, 255, 0), [960, 530, 800, 20])
		pygame.display.flip()

		self.cwvideo = False
		self.playing_cw = False
		self.shvideo = False
		self.playing_sh = False
		self.lavideo = False

		self.current_time = pygame.time.get_ticks()
		self.delay = pygame.time.get_ticks()

		self.surfaceright = pygame.Surface((800, 950))
		self.surfaceright.fill((255, 255, 255))
		self.surfaceright.set_alpha(35)
		self.rect_surfaceright = self.surfaceright.get_rect()
		self.rect_surfaceright.center = 1300, 540
		self.surface_video = pygame.Surface((740, 422))
		self.surface_video.fill((0, 0, 0))
		self.surface_video_rect = self.surface_video.get_rect()
		self.surface_video_rect.center = 1300, 300

	def update_screen(self):

		self.screen.blit(self.background, (0, 0))

		self.screen.blit(self.surfaceright, self.rect_surfaceright)
		self.screen.blit(self.surface_video, self.surface_video_rect)

		self.current_time = pygame.time.get_ticks()
		mouse_coo = pygame.mouse.get_pos()
		police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 50)

		text = [police.render("Bouclier", True, (255, 255, 255)),
				police.render("Onde de choc", True, (255, 255, 255)),
				police.render("TBD", True, (255, 255, 255))]
		text_rects = [i.get_rect() for i in text]

		for i in range(len(text)):
			text_rects[i].left = 390
			text_rects[i].centery = i * 300 + 220
			self.screen.blit(text[i], text_rects[i])

		police = pygame.font.Font("ressource/Police/PIXELITE.ttf", 35)

		text = [police.render("Onde de choc", True, (255, 255, 255))]

		if not self.button_exit_rect.collidepoint(mouse_coo):
			self.screen.blit(self.button_exit, self.button_exit_rect)
		else:
			self.screen.blit(self.button_exit_black, self.button_exit_rect)

		for i in range(len(self.shining_surf)):
			if self.shining_surf_rect[i].collidepoint(mouse_coo):
				self.screen.blit(self.shining_surf[i], self.shining_surf_rect[i])

		if self.shining_surf_rect[1].collidepoint(mouse_coo):
			self.cwvideo = True
		else:
			self.cwvideo = False

		if self.shining_surf_rect[0].collidepoint(mouse_coo):
			self.shvideo = True
		else:
			self.shvideo = False

		if self.shining_surf_rect[0].collidepoint(mouse_coo) and not self.playing_sh:
			self.playing_sh = True
			self.delay = pygame.time.get_ticks()

		if self.shining_surf_rect[1].collidepoint(mouse_coo) and not self.playing_cw:
			self.playing_cw = True
			self.delay = pygame.time.get_ticks()

		if self.shvideo:
			if self.current_time - self.delay > 30:
				if self.index_video_sh < len(self.sh_frames)-1:
					self.index_video_sh += 1
					self.delay = self.current_time
				else:
					self.index_video_sh = 0
					self.delay = self.current_time
			self.current_image_sh = pygame.transform.scale(self.sh_frames[self.index_video_sh], (750, 422))
			self.frame_rect_sh = self.current_image_sh.get_rect()
			self.frame_rect_sh.center = 1300, 300
			self.screen.blit(self.current_image_sh, self.frame_rect_sh)
		else:
			self.index_video_sh = 0
			self.playing_sh = False

		if self.cwvideo:
			if self.current_time - self.delay > 50:
				if self.index_video_cw < len(self.cw_frames)-1:
					self.index_video_cw += 1
					self.delay = self.current_time
				else:
					self.index_video_cw = 0
					self.delay = self.current_time		
			self.current_image_cw = pygame.transform.scale(self.cw_frames[self.index_video_cw], (750, 422))
			self.frame_rect_cw = self.current_image_cw.get_rect()
			self.frame_rect_cw.center = 1300, 300
			self.screen.blit(self.current_image_cw, self.frame_rect_cw)
		else:
			self.index_video_cw = 0 
			self.playing_cw = False

		self.screen.blit(self.image_ability1, self.rect1)
		self.screen.blit(self.image_ability2, self.rect2)
		self.screen.blit(self.image_ability3, self.rect3)





