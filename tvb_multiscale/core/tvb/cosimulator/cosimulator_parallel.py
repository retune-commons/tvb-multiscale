# -*- coding: utf-8 -*-
#
#
#  TheVirtualBrain-Scientific Package. This package holds all simulators, and 
# analysers necessary to run brain-simulations. You can use it stand alone or
# in conjunction with TheVirtualBrain-Framework Package. See content of the
# documentation-folder for more details. See also http://www.thevirtualbrain.org
#
# (c) 2012-2020, Baycrest Centre for Geriatric Care ("Baycrest") and others
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this
# program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#   CITATION:
# When using The Virtual Brain for scientific publications, please cite it as follows:
#
#   Paula Sanz Leon, Stuart A. Knock, M. Marmaduke Woodman, Lia Domide,
#   Jochen Mersmann, Anthony R. McIntosh, Viktor Jirsa (2013)
#       The Virtual Brain: a simulator of primate brain network dynamics.
#   Frontiers in Neuroinformatics (7:10. doi: 10.3389/fninf.2013.00010)
#
#

"""
This is the module responsible for co-simulation of TVB with spiking simulators.
It inherits the Simulator class.

.. moduleauthor:: Dionysios Perdikis <dionysios.perdikis@charite.de>


"""

from tvb_multiscale.core.tvb.cosimulator.cosimulator import CoSimulator


class CoSimulatorParallel(CoSimulator):

    def _run_for_synchronization_time(self, ts, xs, wall_time_start, cosimulation=True, cosim_updates=None, **kwds):
        current_step = int(self.current_step)
        for data in self(cosim_updates=cosim_updates, **kwds):
            for tl, xl, t_x in zip(ts, xs, data):
                if t_x is not None:
                    t, x = t_x
                    tl.append(t)
                    xl.append(x)
        steps_performed = self.current_step - current_step
        return steps_performed


class CoSimulatorMPI(CoSimulatorParallel):

    pass
    # def _run_cosimulation(self, ts, xs, wall_time_start, advance_simulation_for_delayed_monitors_output=True, **kwds):
    #     super(CoSimulatorMPI, self)._run_cosimulation(ts, xs, wall_time_start,
    #                                                   advance_simulation_for_delayed_monitors_output, **kwds)
    #     self.logger.info(" TVB finish")
    #     if self.n_output_interfaces:
    #         logger.info('end comm send')
    #         self.output_interfaces[0].end_mpi()
    #     if self.n_input_interfaces:
    #         logger.info('end comm receive')
    #         self.input_interfaces[0].end_mpi()
    #     self.MPI.Finalize()  # ending with MPI
    #     self.logger.info("TVB exit")
