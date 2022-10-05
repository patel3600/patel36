    clickable = driver.find_element(id: 'clickable')
    driver.action
          .move_to(clickable)
          .pause(duration: 1)
          .click_and_hold
          .pause(duration: 1)
          .send_keys('abc')
          .perform
