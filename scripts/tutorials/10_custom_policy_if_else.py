# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.

from tqdm import trange

import pandemic_simulator as ps
import random


def run_pandemic_gym_env() -> None:
    """Here we execute the gym envrionment wrapped simulator using austin regulations,
    a small town config and default person routines."""

    print('\nA tutorial that runs the OpenAI Gym environment wrapped simulator', flush=True)

    # init globals
    ps.init_globals(seed=104923490)

    # select a simulator config
    sim_config = ps.sh.small_town_config

    # make env

    wrap = ps.env.PandemicGymEnv.from_config(sim_config=sim_config, pandemic_regulations=ps.sh.austin_regulations)

    # setup viz
    viz = ps.viz.GymViz.from_config(sim_config=sim_config)
    sim_viz = ps.viz.SimViz.from_config(sim_config=sim_config)

    # run stage-0 action steps in the environment
    wrap.reset()
    Reward = 0
    for i in trange(120, desc='Simulating day'):

        if i == 0:
            action = 0

        else:
            # if i%10==0:
            #     viz.plot()
            #     sim_viz.plot()

            #######################################################################################################################################
            # #Replace the code in the below if-else statement with your own policy, based on observation variables
            # if obs.time_day[...,0]>20:
            #     action = 1
            # elif not obs.infection_above_threshold:
            #     action = 0
            # else:
            #     action = 4

            # Number of people in Infected condition according to current testing policy
            if obs.global_testing_summary[..., 2] > 400:
                action = 4
            elif obs.global_testing_summary[..., 2] > 200:
                action = 3
            elif obs.global_testing_summary[..., 2] > 100:
                action = 2
            elif obs.global_testing_summary[..., 2] > 50:
                action = 1
            # Number of people in Infected condition according to current testing policy
           
            # Number of people in Infected condition according to current testing policy            
            
            elif not obs.infection_above_threshold:
                action = 0
            ########################################################################################################################################

        # here the action is the discrete regulation stage identifier
        obs, reward, done, aux = wrap.step(action=int(action))
        # print(obs)
        Reward += reward
        viz.record((obs, reward))
        sim_viz.record_state(state=wrap.pandemic_sim.state)
    # generate plots
    viz.plot()
    sim_viz.plot()
    print('Reward:'+str(Reward))


if __name__ == '__main__':
    run_pandemic_gym_env()
