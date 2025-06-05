import numpy as np 
import matplotlib.pyplot as plt

def setup_boundary(u) :
    u[0,:] = 100
    u[-1,:] = 100
    u[30,:] = 100

#defining our problem
if __name__ == "__main__":
    alpha = 0.05     # thermal diffusivity
    Lx, Ly = 1, 1 # domain size
    Tmax = 1    # Total simulation time
    Nx, Ny = 60, 60 # number of spatial nodes

    #Initalization

    dx = Lx/(Nx-1)
    dy = Ly/(Ny-1)
    
    dt = (1/(2*alpha))*((1/dx**2)+(1/dy**2))**-1    # stability condition (explicit method)
    Nt = int(Tmax/dt)  #number of time steps
    u = np.zeros((Nx,Ny)) + 20    #plate is initially as 20 degrees C

    #boundary conditions

    setup_boundary(u)

    #visualizing with  a plot
    fig, axis  = plt.subplots(figsize=(10, 8))

    pcm = axis.pcolormesh(u, cmap = plt.cm.jet, vmin = 0, vmax = 100)
    plt.colorbar(pcm, ax = axis)
    axis.set_title("Initial Temperature Distribution")
    #simulating

    plt.pause(5)

    counter = 0
    while counter<Tmax:
        w = u.copy()

        for i in range(1, Nx -1):
            for j in range(1, Ny -1):

                dd_ux = (w[i-1,j] - 2*w[i,j] + w[i+1,j])/dx**2
                dd_uy = (w[i,j-1] - 2*w[i,j] + w[i,j+1])/dy**2

                u[i,j] = dt * alpha * (dd_ux + dd_uy) + w[i,j]
                #update heat resource:
                setup_boundary(u)

        counter += dt 
        print("t: {:.3f}[s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

        #updating the plot

        pcm.set_array(u)
        axis.set_title("Distribution at t: {:.3f}[s].".format(counter))
        plt.pause(0.01)


    plt.show()