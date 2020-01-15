/**
 * Adherent
 * Adherent api
 *
 * OpenAPI spec version: 1.0.0
 *
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *//* tslint:disable:no-unused-variable member-ordering */

import { Inject, Injectable, Optional }                      from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams,
         HttpResponse, HttpEvent }                           from '@angular/common/http';
import { CustomHttpUrlEncodingCodec }                        from '../encoder';

import { Observable }                                        from 'rxjs';

import { Port } from '../model/port';

import { BASE_PATH, COLLECTION_FORMATS }                     from '../variables';
import { Configuration }                                     from '../configuration';


@Injectable()
export class PortService {

    protected basePath = '/api';
    public defaultHeaders = new HttpHeaders();
    public configuration = new Configuration();

    constructor(protected httpClient: HttpClient, @Optional()@Inject(BASE_PATH) basePath: string, @Optional() configuration: Configuration) {
        if (basePath) {
            this.basePath = basePath;
        }
        if (configuration) {
            this.configuration = configuration;
            this.basePath = basePath || configuration.basePath || this.basePath;
        }
    }

    /**
     * @param consumes string[] mime-types
     * @return true: consumes contains 'multipart/form-data', false: otherwise
     */
    private canConsumeForm(consumes: string[]): boolean {
        const form = 'multipart/form-data';
        for (const consume of consumes) {
            if (form === consume) {
                return true;
            }
        }
        return false;
    }


    /**
     * Check whether MAB is enable on this port or not.
     *
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public mabGet(portId: number, observe?: 'body', reportProgress?: boolean): Observable<boolean>;
    public mabGet(portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<boolean>>;
    public mabGet(portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<boolean>>;
    public mabGet(portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling mabGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<boolean>('get',`${this.basePath}/port/${encodeURIComponent(String(portId))}/mab/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Filter ports
     *
     * @param limit Limit the number of ports returned in the result. Default is 100
     * @param offset Skip the first n results
     * @param switchID Filter only ports from that switch
     * @param roomNumber Filter only ports from that room
     * @param terms Search terms
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portGet(limit?: number, offset?: number, switchID?: number, roomNumber?: number, terms?: string, observe?: 'body', reportProgress?: boolean): Observable<Array<Port>>;
    public portGet(limit?: number, offset?: number, switchID?: number, roomNumber?: number, terms?: string, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Array<Port>>>;
    public portGet(limit?: number, offset?: number, switchID?: number, roomNumber?: number, terms?: string, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Array<Port>>>;
    public portGet(limit?: number, offset?: number, switchID?: number, roomNumber?: number, terms?: string, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {






        let queryParameters = new HttpParams({encoder: new CustomHttpUrlEncodingCodec()});
        if (limit !== undefined && limit !== null) {
            queryParameters = queryParameters.set('limit', <any>limit);
        }
        if (offset !== undefined && offset !== null) {
            queryParameters = queryParameters.set('offset', <any>offset);
        }
        if (switchID !== undefined && switchID !== null) {
            queryParameters = queryParameters.set('switchID', <any>switchID);
        }
        if (roomNumber !== undefined && roomNumber !== null) {
            queryParameters = queryParameters.set('roomNumber', <any>roomNumber);
        }
        if (terms !== undefined && terms !== null) {
            queryParameters = queryParameters.set('terms', <any>terms);
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<Array<Port>>('get',`${this.basePath}/port/`,
            {
                params: queryParameters,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Delete a port
     *
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdDelete(portId: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPortIdDelete(portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPortIdDelete(portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPortIdDelete(portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdDelete.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<any>('delete',`${this.basePath}/port/${encodeURIComponent(String(portId))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve a port
     *
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdGet(portId: number, observe?: 'body', reportProgress?: boolean): Observable<Port>;
    public portPortIdGet(portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<Port>>;
    public portPortIdGet(portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<Port>>;
    public portPortIdGet(portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<Port>('get',`${this.basePath}/port/${encodeURIComponent(String(portId))}`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Enable/disable MAB on a port
     *
     * @param body
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdMabPut(body: boolean, portId: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPortIdMabPut(body: boolean, portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPortIdMabPut(body: boolean, portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPortIdMabPut(body: boolean, portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling portPortIdMabPut.');
        }

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdMabPut.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('put',`${this.basePath}/port/${encodeURIComponent(String(portId))}/mab/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Update a port
     *
     * @param body Port to update
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdPut(body: Port, portId: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPortIdPut(body: Port, portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPortIdPut(body: Port, portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPortIdPut(body: Port, portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling portPortIdPut.');
        }

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdPut.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('put',`${this.basePath}/port/${encodeURIComponent(String(portId))}`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Shutdown/enable a port
     *
     * @param body True to open, False to shutdown
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdStatePut(body: boolean, portId: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPortIdStatePut(body: boolean, portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPortIdStatePut(body: boolean, portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPortIdStatePut(body: boolean, portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling portPortIdStatePut.');
        }

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdStatePut.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('put',`${this.basePath}/port/${encodeURIComponent(String(portId))}/state/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Change the VLAN assigned a to port
     *
     * @param body VLAN to assign. Set it to 1 if you want to enable authentication on the port.
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPortIdVlanPut(body: number, portId: number, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPortIdVlanPut(body: number, portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPortIdVlanPut(body: number, portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPortIdVlanPut(body: number, portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling portPortIdVlanPut.');
        }

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling portPortIdVlanPut.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('put',`${this.basePath}/port/${encodeURIComponent(String(portId))}/vlan/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Create a port
     *
     * @param body Port to create
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public portPost(body: Port, observe?: 'body', reportProgress?: boolean): Observable<any>;
    public portPost(body: Port, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<any>>;
    public portPost(body: Port, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<any>>;
    public portPost(body: Port, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (body === null || body === undefined) {
            throw new Error('Required parameter body was null or undefined when calling portPost.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
            'application/json'
        ];
        const httpContentTypeSelected: string | undefined = this.configuration.selectHeaderContentType(consumes);
        if (httpContentTypeSelected != undefined) {
            headers = headers.set('Content-Type', httpContentTypeSelected);
        }

        return this.httpClient.request<any>('post',`${this.basePath}/port/`,
            {
                body: body,
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve the status of a port.
     *
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public stateGet(portId: number, observe?: 'body', reportProgress?: boolean): Observable<boolean>;
    public stateGet(portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<boolean>>;
    public stateGet(portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<boolean>>;
    public stateGet(portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling stateGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<boolean>('get',`${this.basePath}/port/${encodeURIComponent(String(portId))}/state/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

    /**
     * Retrieve the VLAN assigned to the port.
     *
     * @param portId
     * @param observe set whether or not to return the data Observable as the body, response or events. defaults to returning the body.
     * @param reportProgress flag to report request and response progress.
     */
    public vlanGet(portId: number, observe?: 'body', reportProgress?: boolean): Observable<number>;
    public vlanGet(portId: number, observe?: 'response', reportProgress?: boolean): Observable<HttpResponse<number>>;
    public vlanGet(portId: number, observe?: 'events', reportProgress?: boolean): Observable<HttpEvent<number>>;
    public vlanGet(portId: number, observe: any = 'body', reportProgress: boolean = false ): Observable<any> {

        if (portId === null || portId === undefined) {
            throw new Error('Required parameter portId was null or undefined when calling vlanGet.');
        }

        let headers = this.defaultHeaders;

        // to determine the Accept header
        let httpHeaderAccepts: string[] = [
            'application/json'
        ];
        const httpHeaderAcceptSelected: string | undefined = this.configuration.selectHeaderAccept(httpHeaderAccepts);
        if (httpHeaderAcceptSelected != undefined) {
            headers = headers.set('Accept', httpHeaderAcceptSelected);
        }

        // to determine the Content-Type header
        const consumes: string[] = [
        ];

        return this.httpClient.request<number>('get',`${this.basePath}/port/${encodeURIComponent(String(portId))}/vlan/`,
            {
                withCredentials: this.configuration.withCredentials,
                headers: headers,
                observe: observe,
                reportProgress: reportProgress
            }
        );
    }

}
