#Yang Tang 53979886
import mapquest_input
import mapquest_output

def number_of_inputs():
    '''stores the inputs into lists of strings'''
    number=int(input())
    if number<2:
        print('ERROR')
        return number_of_inputs()
    inputs_list=[]
    for i in range(number):
        inputs_list.append(input())
    return inputs_list

def number_of_outputs():
    '''stores the outputs into lists of strings'''
    number=int(input())
    if number<0 or number>5:
        print('ERROR')
        return number_of_outputs()
    outputs_list=[]
    for i in range(number):
        outputs_list.append(input())
    return outputs_list

def main_function(outputs:list):
    l=[]
    for i in outputs:
        if i.lower()=='steps':
            l.append(mapquest_output.steps())
        if i.lower()=='totaltime':
            l.append(mapquest_output.total_time())
        if i.lower()=='totaldistance':
            l.append(mapquest_output.total_distance())
        if i.lower()=='latlong':
            l.append(mapquest_output.lat_long())
        if i.lower()=='elevation':
            l.append(mapquest_output.elevation())
    return l

def user_interface():
    inputs=number_of_inputs()
    outputs=number_of_outputs()
    url=mapquest_input.build_mapquest_url(inputs)
    route=mapquest_input.get_result(url)
    no_route_error=False
    other_error=False
    status_code=route['info']['statuscode']
    if status_code in [402,612]:
        no_route_error=True
    elif status_code != 0:
        other_error=True
    if no_route_error:
        print('NO ROUTE FOUND')
    elif other_error:
        print('MAPQUEST ERROR')
    else:
        for i in main_function(outputs):
            i.output_self(route)
        print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors.')

 
if __name__ == "__main__":
    user_interface()
